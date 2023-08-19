#!/usr/bin/env python3

import DaVinciResolveScript as dvr_script
resolve = dvr_script.scriptapp("Resolve")

ProjectManager = resolve.GetProjectManager()
Project = ProjectManager.GetCurrentProject()
MediaStorage = resolve.GetMediaStorage()
MediaPool = Project.GetMediaPool()
RootFolder = MediaPool.GetRootFolder()
MediaPool.GetRootFolder()

Clips = RootFolder.GetClipList()
for clip in Clips:
    clip.SetClipProperty('Start TC', '00:00:00:00')


