#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : qt6virtualkeyboard
Version  : 6.6.0
Release  : 2
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtvirtualkeyboard-everywhere-src-6.6.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtvirtualkeyboard-everywhere-src-6.6.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear GFDL-1.3 GPL-3.0
Requires: qt6virtualkeyboard-lib = %{version}-%{release}
Requires: qt6virtualkeyboard-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(hunspell)
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
BuildRequires : qt6svg-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Qt Virtual Keyboard
Qt Virtual Keyboard is a virtual keyboard framework that consists of a C++
backend supporting custom input methods as well as a UI frontend implemented
in QML.

%package dev
Summary: dev components for the qt6virtualkeyboard package.
Group: Development
Requires: qt6virtualkeyboard-lib = %{version}-%{release}
Provides: qt6virtualkeyboard-devel = %{version}-%{release}
Requires: qt6virtualkeyboard = %{version}-%{release}

%description dev
dev components for the qt6virtualkeyboard package.


%package lib
Summary: lib components for the qt6virtualkeyboard package.
Group: Libraries
Requires: qt6virtualkeyboard-license = %{version}-%{release}

%description lib
lib components for the qt6virtualkeyboard package.


%package license
Summary: license components for the qt6virtualkeyboard package.
Group: Default

%description license
license components for the qt6virtualkeyboard package.


%prep
%setup -q -n qtvirtualkeyboard-everywhere-src-6.6.0
cd %{_builddir}/qtvirtualkeyboard-everywhere-src-6.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697215071
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697215071
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/openwnn/3rdparty/openwnn/NOTICE %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/0ad70704f3dc3c6cee594f035b21168238e08b85 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/pinyin/3rdparty/pinyin/NOTICE %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/e4842b59eeb67867c51032209565509e0fc589b5 || :
cp %{_builddir}/qtvirtualkeyboard-everywhere-src-%{version}/src/plugins/tcime/3rdparty/tcime/COPYING %{buildroot}/usr/share/package-licenses/qt6virtualkeyboard/c42470b2f854bca72da8965f9549c431a9475e5a || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6hunspellinputmethod_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6virtualkeyboard_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_hunspellinputmethod.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_hunspellinputmethod_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_virtualkeyboard.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_virtualkeyboard_private.pri
/usr/lib64/qt6/modules/HunspellInputMethod.json
/usr/lib64/qt6/modules/VirtualKeyboard.json
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/AlternativeKeys.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/BackspaceKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/BaseKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/ChangeLanguageKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/CharacterPreviewBubble.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/EnterKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/FillerKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/FlickKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/FunctionPopupList.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/HandwritingModeKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/HideKeyboardKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/InputModeKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/Key.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/Keyboard.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/KeyboardColumn.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/KeyboardLayout.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/KeyboardLayoutLoader.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/KeyboardRow.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/ModeKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/MultiSoundEffect.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/MultitapInputMethod.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/NumberKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/PopupList.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/SelectionControl.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/ShadowInputControl.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/ShiftKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/SpaceKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/SymbolModeKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/TraceInputArea.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/TraceInputKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/WordCandidatePopupList.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/qtvkbcomponentsplugin.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/EnterKey.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/HandwritingInputPanel.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/InputPanel.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Layouts/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Layouts/qtvkblayoutsplugin.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hangul/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hangul/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hunspell/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hunspell/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/OpenWNN/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/OpenWNN/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Pinyin/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Pinyin/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/TCIme/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/TCIme/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Thai/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Thai/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/qtvkbpluginsplugin.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Settings/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Settings/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/Builtin/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/Builtin/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/KeyIcon.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/KeyPanel.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/KeyboardStyle.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/SelectionListItem.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/TraceCanvas.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/TraceInputKeyPanel.qml
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/TraceUtils.js
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/qmldir
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtHunspellInputMethod/6.6.0/QtHunspellInputMethod/private/hunspellinputmethod_p.h
/usr/include/QtHunspellInputMethod/6.6.0/QtHunspellInputMethod/private/hunspellinputmethod_p_p.h
/usr/include/QtHunspellInputMethod/6.6.0/QtHunspellInputMethod/private/hunspellwordlist_p.h
/usr/include/QtHunspellInputMethod/6.6.0/QtHunspellInputMethod/private/hunspellworker_p.h
/usr/include/QtHunspellInputMethod/6.6.0/QtHunspellInputMethod/private/qthunspellinputmethodexports_p.h
/usr/include/QtHunspellInputMethod/QtHunspellInputMethod
/usr/include/QtHunspellInputMethod/QtHunspellInputMethodDepends
/usr/include/QtHunspellInputMethod/QtHunspellInputMethodVersion
/usr/include/QtHunspellInputMethod/qhunspellinputmethod_global.h
/usr/include/QtHunspellInputMethod/qthunspellinputmethodexports.h
/usr/include/QtHunspellInputMethod/qthunspellinputmethodversion.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/abstractinputpanel_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/appinputpanel_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/appinputpanel_p_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/desktopinputpanel_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/desktopinputselectioncontrol_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/enterkeyaction_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/enterkeyactionattachedtype_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/fallbackinputmethod_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/gesturerecognizer_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/handwritinggesturerecognizer_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/inputmethod_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/inputselectionhandle_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/inputview_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/plaininputmethod_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/platforminputcontext_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qtvirtualkeyboard-config_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qtvirtualkeyboardexports_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qvirtualkeyboardabstractinputmethod_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qvirtualkeyboardfeatures_namespace_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/qvirtualkeyboardnamespace_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/settings_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/shadowinputcontext_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/shifthandler_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/virtualkeyboard_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/virtualkeyboardattachedtype_p.h
/usr/include/QtVirtualKeyboard/6.6.0/QtVirtualKeyboard/private/virtualkeyboarddebug_p.h
/usr/include/QtVirtualKeyboard/QVirtualKeyboardAbstractInputMethod
/usr/include/QtVirtualKeyboard/QVirtualKeyboardDictionary
/usr/include/QtVirtualKeyboard/QVirtualKeyboardDictionaryManager
/usr/include/QtVirtualKeyboard/QVirtualKeyboardInputContext
/usr/include/QtVirtualKeyboard/QVirtualKeyboardInputEngine
/usr/include/QtVirtualKeyboard/QVirtualKeyboardObserver
/usr/include/QtVirtualKeyboard/QVirtualKeyboardSelectionListModel
/usr/include/QtVirtualKeyboard/QVirtualKeyboardTrace
/usr/include/QtVirtualKeyboard/QtVirtualKeyboard
/usr/include/QtVirtualKeyboard/QtVirtualKeyboardDepends
/usr/include/QtVirtualKeyboard/QtVirtualKeyboardVersion
/usr/include/QtVirtualKeyboard/qtvirtualkeyboard-config.h
/usr/include/QtVirtualKeyboard/qtvirtualkeyboardexports.h
/usr/include/QtVirtualKeyboard/qtvirtualkeyboardversion.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboard_global.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboard_namespace.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardabstractinputmethod.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboarddictionary.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboarddictionarymanager.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardinputcontext.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardinputengine.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardobserver.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardselectionlistmodel.h
/usr/include/QtVirtualKeyboard/qvirtualkeyboardtrace.h
/usr/lib64/cmake/Qt6/FindCerenceHwrAlphabetic.cmake
/usr/lib64/cmake/Qt6/FindCerenceHwrCjk.cmake
/usr/lib64/cmake/Qt6/FindCerenceXt9.cmake
/usr/lib64/cmake/Qt6/FindHunspell.cmake
/usr/lib64/cmake/Qt6/FindMyScript.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtVirtualKeyboardTestsConfig.cmake
/usr/lib64/cmake/Qt6BundledOpenwnn/Qt6BundledOpenwnnDependencies.cmake
/usr/lib64/cmake/Qt6BundledPinyin/Qt6BundledPinyinDependencies.cmake
/usr/lib64/cmake/Qt6BundledTcime/Qt6BundledTcimeDependencies.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginConfig.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Gui/Qt6QVirtualKeyboardPluginTargets.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodConfig.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodConfigVersion.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodDependencies.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodTargets.cmake
/usr/lib64/cmake/Qt6HunspellInputMethod/Qt6HunspellInputMethodVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbbuiltinstylespluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbcomponentspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhangulpluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbhunspellpluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkblayoutspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbopenwnnpluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpinyinpluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbpluginspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbsettingspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbstylespluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbtcimepluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtvkbthaipluginTargets.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardConfig.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardConfigVersion.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardDependencies.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardTargets.cmake
/usr/lib64/cmake/Qt6VirtualKeyboard/Qt6VirtualKeyboardVersionlessTargets.cmake
/usr/lib64/libQt6HunspellInputMethod.prl
/usr/lib64/libQt6HunspellInputMethod.so
/usr/lib64/libQt6VirtualKeyboard.prl
/usr/lib64/libQt6VirtualKeyboard.so
/usr/lib64/pkgconfig/Qt6HunspellInputMethod.pc
/usr/lib64/pkgconfig/Qt6VirtualKeyboard.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6HunspellInputMethod.so.6
/usr/lib64/libQt6HunspellInputMethod.so.6.6.0
/usr/lib64/libQt6VirtualKeyboard.so.6
/usr/lib64/libQt6VirtualKeyboard.so.6.6.0
/usr/lib64/qt6/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Components/libqtvkbcomponentsplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Layouts/libqtvkblayoutsplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hangul/libqtvkbhangulplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Hunspell/libqtvkbhunspellplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/OpenWNN/libqtvkbopenwnnplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Pinyin/libqtvkbpinyinplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/TCIme/libqtvkbtcimeplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/Thai/libqtvkbthaiplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Plugins/libqtvkbpluginsplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Settings/libqtvkbsettingsplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/Builtin/libqtvkbbuiltinstylesplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/Styles/libqtvkbstylesplugin.so
/usr/lib64/qt6/qml/QtQuick/VirtualKeyboard/libqtvkbplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6virtualkeyboard/0ad70704f3dc3c6cee594f035b21168238e08b85
/usr/share/package-licenses/qt6virtualkeyboard/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6virtualkeyboard/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6virtualkeyboard/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6virtualkeyboard/c42470b2f854bca72da8965f9549c431a9475e5a
/usr/share/package-licenses/qt6virtualkeyboard/e4842b59eeb67867c51032209565509e0fc589b5
