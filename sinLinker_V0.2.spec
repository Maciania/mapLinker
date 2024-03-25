# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/map_linker_xml/main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/map_linker_xml/SinLib.py', '.'), ('D:/map_linker_xml/map.py', '.'), ('D:/map_linker_xml/sin_logo.png', '.'), ('D:/map_linker_xml/omx.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='sinLinker_V0.2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\map_linker_xml\\sin_logo.ico'],
)
