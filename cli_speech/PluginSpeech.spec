# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PluginSpeech.py'],
             pathex=['Z:\\src'],
             binaries=[],
             datas=[('/cert/roots.pem', 'grpc/_cython/_credentials')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PluginSpeech',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='icon_speech.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PluginSpeech')
