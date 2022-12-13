# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = []

# TARGET
target = Executable(
    script="URPHelper.py",
    # base="Win32GUI",
    icon="Asserts/favicon.ico"
)

# SETUP CX FREEZE
setup(
    name="SCU URP Helper",
    version="0.3.2",
    description="四川大学教务处系统助手",
    author="Pikachu IM https://github.com/PIKACHUIM/UrpHelps",
    options={'build_exe': {'include_files': files}},
    executables=[target],
)
