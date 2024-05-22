[app]
# (str) Title of your application
title = YOLOv8App

# (str) Package name
package.name = yolov8app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of permissions to grant to the app (see https://developer.android.com/reference/android/Manifest.permission)
android.permissions = CAMERA

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,numpy,opencv-python,torch,torchvision,ultralytics,certifi

# (str) Android NDK version to use
android.ndk = 25

# (bool) Indicate whether the application should be compiled in debug mode
# (you may need to set it to 0 for a release build)
android.debug = 1

# (str) Application versioning (method 1)
version = 0.1

#Android sdk manager path
android.sdk_path = ~/android-sdk

source.include_exts = py,png,jpg,kv,atlas,txt,md,json,xml
# If using setup.py:
source.include_patterns = setup.py
