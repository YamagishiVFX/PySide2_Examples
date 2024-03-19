"""モジュールの説明タイトル
 
* ソースコードの一番始めに記載すること
* importより前に記載する

Info:
    * Created : 2023/12/06 Tatsuya YAMAGISHI
    * Coding : Python 3.10.11 & PySide2
    * Client: Maya 2024.2 EN
    * Author:  Copyright (C) Spade&Co.Inc. All Rights Reserved.


Release Note:
    * v1.1.1 2024/02/09 Yamagishi
        * NEW
            * Import > ShaderBall

        * UPDATED
            * renamed : shapde_workflow => spahde_assetlibs

    * v1.1.0 2024/01/15 Yamagishi
        * NEW
            * Import Camera 追加

    * v1.0.0 2023/12/06 Yamagishi
        * New
            * Import Asset メニュー
"""

VERSION = 'v1.1.0'
NAME = 'sp_menu'

# -------------------------------------
# import
# -------------------------------------

import maya.cmds as cmds
import maya.mel as mel
import maya.utils as utils

from textwrap import dedent

# -------------------------------------
# Settings
# -------------------------------------
# -------------------------------------
# setup
# -------------------------------------

def setup():
    menu_sp_global = "spade_menu"
    labelMenu = "Spade"
    
    # MainMenu
    if cmds.menu( menu_sp_global, l=labelMenu, p='MayaWindow' ) != 0:
        cmds.deleteUI( cmds.menu(menu_sp_global, l=labelMenu, e=1, dai=1, vis=1 ) )

    cmds.refresh()

    sp_main_menu = cmds.menu(menu_sp_global, l=labelMenu, p='MayaWindow', to=1, aob=True)


    # File
    cmds.menuItem(l='File', d=True)

    # Asset
    cmds.menuItem(l='Asset', d=True)
    cmds.menuItem(l='Import', subMenu=True)
    cmds.menuItem(
                l='Asset Structure', c='import spade_assetlibs;spade_assetlibs.import_asset_template(spp)')
    cmds.menuItem(
                l='Camera', c='spp.import_assetlib("camera_rig_maya")')
    cmds.menuItem(
                l='Humans', c='spp.import_assetlib("std_human")')
    cmds.menuItem(
                l='ShaderBall', c='spp.import_assetlib("shaderball")')
    cmds.setParent( '..', menu=True )

    # Texure
    cmds.menuItem(l='Shader', d=True)
    cmds.menuItem(l='File Texture Manager', c='mel.eval("FileTextureManager")', p=sp_main_menu)
    #cmds.menuItem(l='UDIM', c='mel.eval("generateAllUvTilePreviews")', p=sp_main_menu)

    cmds.menuItem(l='PlayBlast', d=True)
    cmds.menuItem(l='FastPB', c='import fastfb_main as pb; pb.main("Maya")', p=sp_main_menu, i='fastPB.png')

    # Riggings
    cmds.menuItem(l='Rigging', d=True)
    # SI Weight Editor
    cmds.menuItem(
    label='SiWeightEditor',
    annotation="open SiWeightEditor",
    parent=sp_main_menu ,
    echoCommand=True,
    command=dedent(
        '''
            import siweighteditor.siweighteditor
            siweighteditor.siweighteditor.Option()
        ''')
    )

    # Rig
    cmds.menuItem(l='Animation', d=True)
    cmds.menuItem(l='Dream Wall Picker', c='import dwpicker;dwpicker.show()', p=sp_main_menu)
    cmds.menuItem(l='MoxRig Controller', c='mel.eval("MoxRigController")', p=sp_main_menu)
    cmds.menuItem(l='StudioLibrary', c='import load_studiolibrary as st;st.load()', p=sp_main_menu, i='studiolibrary_icon.png')


    # Utility
    cmds.menuItem(l='Utility', d=True)
    cmds.menuItem(l='Module Manager', c='import module_manager.ui; module_manager.ui.show()', p=sp_main_menu, i='MM_icon.png')
