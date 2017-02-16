# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import traceback
import time

import maya.cmds as cmds
import pymel.core as pm
import pprint

import tank
from tank import Hook

from datetime import datetime 
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

class PostPlayblast(Hook):
    """
    Hook called when a file needs to be copied
    """
    
    def execute(self, action="", data=[], **kwargs):
        """
        Main hook entry point
        
        :action:        String
                        copy_file           -> copy QTfiles to locations in config
                        create_version      -> register a new Version entity in Shotgun or update existing Version
                        upload_move         -> upload generated QT file to Shotgun
        """
        # get the application and it's shotgun instance
        app = self.parent
        sg = app.sgtk.shotgun

        print data


        if action == "copy_file":
            try:

                self.make_runme_batchfile(data)

            except Exception, e:
                print e
                print "Error in copying data to review folder "
                return False

            return True

        elif action == "create_version":
            """ 
                Setting up shotgun version entity without uploading the QT file
            """
            currentDatetime = datetime.now().strftime(TIMESTAMP_FORMAT)
            descriptionForm = "%(comment)s\n\nPublish by %(username)s at %(hostname)s on %(datetime)s"
            data['description'] = descriptionForm % dict(
                comment=data['description'],
                datetime=currentDatetime,
                username=os.environ.get("USERNAME", "unknown"),
                hostname=os.environ.get("COMPUTERNAME", "unknown"))
            app.log_debug("Setting up shotgun version entity...")
            
            try:
                filters = [ ["Project", "is", data["project"]],
                            ["code", "is", data["code"]],
                            ]
                # check if a version entity with same code exists in shotgun
                # if none, create a new version Entity with qtfile name as its code
                result=None

                app.log_debug("Create a new Version as %s" % data["code"])

                result = sg.create('Version', data)

            except:
                app.log_debugresult("Something wrong")
                traceback.print_exc()
                return  False
            return True


        elif action == "log_time":
            """
                Setting up shotgun version entity without uploading the QT file
            """
            app.log_debug("Setting up shotgun time log entity...")

            try:

                result = None
                app.log_debug("Create a new Time log for %s" % data["entity"])

                result = sg.create("TimeLog", {"duration": data['duration'],
                                                "entity": app.context.task,
                                                "project": app.context.project})
            except Exception, e:
                print ("Something wrong failed to log time consumed\n")
                print e
                traceback.print_exc()
                return False
            return True
        
        elif action == "check_version":
            """ 
                Setting up shotgun version entity without uploading the QT file
            """
            app.log_debug("checking up shotgun version entity...")
            result = False
            try:
                filters = [ ["Project", "is", data["project"]],
                            ["code", "is", data["code"]],
                            ]
                # check if a version entity with same code exists in shotgun
                # if none, create a new version Entity with qtfile name as its code
                version = sg.find_one("Version", [["code", "is", data["code"]]])
                if version:
                    app.log_debug("Version already exist")
                    print ("Version already exist %s " % version)
                    result = True
            except:
                app.log_debug("Something wrong")
                traceback.print_exc()
            return result

        elif action == "upload_movie":
            """
                Sending it to shotgun
            """
            app.log_debug("Send qtfile to Shotgun")
            try:
                moviePath = data["path"]
                filters =[ ["Project", "is", data["project"]],
                           ["id", "is", data["version_id"]],
                           ]
                result=None
                if os.path.exists(moviePath):
                    app.log_debug("Uploading movie to Shotgun: %s" % moviePath)
                    result=sg.upload("Version", data["version_id"], moviePath, field_name="sg_uploaded_movie")
                return result
            except:
                app.log_debug("Something wrong")
                traceback.print_exc()

        else:
            app.log_debug("nothing to do")




    def make_runme_batchfile(self,data):
        """

        :param data:
        :return:
        """

        TIMESTAMP_FORMAT = "%Y_%m_%d_%H_%M_%S"

        makeDir = False
        now = datetime.now().strftime(TIMESTAMP_FORMAT)
        runme_temp_path = os.environ['TEMP'] + '\\runme_' + now + '.bat'
        review_dir = data['review_dir']
        review_file = data['review_file']
        try:
            if not os.path.exists(review_dir):
                makeDir = True

            if os.path.exists(runme_temp_path):
                os.remove(runme_temp_path)

            with open(runme_temp_path, 'w') as runme:
                if makeDir:
                    runme.write('mkdir "%s" \n' % (review_dir.replace('V:', '\\\\vg_server\Project')))
                for src in data['review_images']:
                    runme.write('copy "%s" "%s" /Y \n' % (src, review_dir.replace('V:', '\\\\vg_server\Project')))
                runme.write('copy "%s" "%s" /Y \n' % (review_file.replace('/', '\\'), review_dir.replace('V:', '\\\\vg_server\Project')))

            os.system("S:\\softwares\\shotgun\\studio\\admin.exe %s" % runme_temp_path)
            time.sleep(3)

        except:
            os.remove(runme_temp_path)
            return False

        return runme_temp_path