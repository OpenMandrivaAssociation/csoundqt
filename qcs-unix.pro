!unix:error(This project file is only for Unix-based systems.)
!no_messages {
	message()
	message(Building CsoundQt for Unix-based system.)
}

# Set default paths
DEFAULT_CSOUND_API_INCLUDE_DIRS += /usr/local/include/csound \
	/usr/include/csound
DEFAULT_CSOUND_INTERFACES_INCLUDE_DIRS += $${DEFAULT_CSOUND_API_INCLUDE_DIRS}
DEFAULT_CSOUND_LIBRARY_DIRS += /usr/lib \
	/usr/lib64
DEFAULT_LIBSNDFILE_INCLUDE_DIRS += /usr/include
DEFAULT_LIBSNDFILE_LIBRARY_DIRS += /usr/lib \
    /usr/lib64
build32:DEFAULT_CSOUND_LIBS = libcsound.so \
	libcsound.a
build64:DEFAULT_CSOUND_LIBS = libcsound.so \
	libcsound.a
LIBSNDFILE_LIB = libsndfile.so

DEFAULT_PYTHON_INCLUDE_DIR += /usr/local/include \
    /usr/include
DEFAULT_PYTHONQT_LIBRARY_DIRS += /usr/local/lib \
        /usr/lib\
        ../../../PythonQt2.0.1 \
        ../PythonQt2.0.1 \
        PythonQt2.0.1
QCS_QT5 {
DEFAULT_PYTHONQT_SRC_DIRS += ../../../PythonQt \
        ../PythonQt \
        PythonQt
PYTHONQT_LIB_DIR=/usr/local/lib
#PYTHONQT_LIB += PythonQt5_QtAll$${DEBUG_EXT}
PYTHONQT_LIB += PythonQt5
} else {
DEFAULT_PYTHONQT_SRC_DIRS += ../../../PythonQt2.0.1 \
        ../PythonQt2.0.1 \
        PythonQt2.0.1
#PYTHONQT_LIB += PythonQt_QtAll$${DEBUG_EXT}
PYTHONQT_LIB += PythonQt

}

DEFAULT_PORTMIDI_DIR +=  /usr/include

# Do configuration step
include(config.pri)

# Use results from config step
LIBS *= -L$${CSOUND_LIBRARY_DIR}
LIBS *= -L$${LIBSNDFILE_LIBRARY_DIR}
rtmidi {
DEFINES += __LINUX_ALSASEQ__
DEFINES += __LINUX_ALSA__
LIBS += -lasound
}
quteapp_f {
message(Bundling QuteApp_f)
RESOURCES += "src/quteapp_f.qrc"
}
quteapp_d {
message(Bundling QuteApp_d)
RESOURCES += "src/quteapp_d.qrc"
}
build32:LCSOUND = -lcsound
build64:LCSOUND = -lcsound64

csound6: LCSND = -lcsnd6
else: LCSND = -lcsnd
LSNDFILE = -lsndfile

