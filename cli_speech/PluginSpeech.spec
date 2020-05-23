# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PluginSpeech.py'],
             pathex=['google', '/home/juniordev/.autopsy/dev/python_modules/SpeechAudio/cli_speech'],
             binaries=[],
             datas=[],
             hiddenimports=['google'],
             hookspath=['/home/juniordev/.autopsy/dev/python_modules/SpeechAudio/cli_speech/hooks'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PluginSpeech',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
