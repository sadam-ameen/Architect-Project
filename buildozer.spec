[app]
# (str) Title of your application
title = Architect System

# (str) Package name
package.name = architect_bypass

# (str) Package domain (needed for android packaging)
package.domain = org.architect

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# تأكد من إضافة الـ requirements الأساسية لعمل الكود
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# بما أن التطبيق يستخدم الـ Sockets والاتصال، يحتاج صلاحية الإنترنت
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

