#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: System
# Generated: Fri Aug  5 18:38:12 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from decode import decode  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from rx import rx  # grc-generated hier_block
from tx import tx  # grc-generated hier_block
import sip


class system(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "System")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("System")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "system")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.tx_0 = tx(
            samp_rate=samp_rate,
        )
        self.top_layout.addWidget(self.tx_0)
        self.rx_0 = rx(
            samp_rate=samp_rate,
        )
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_char,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            3
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_0.set_min(i, -128)
            self.qtgui_number_sink_0.set_max(i, 128)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.decode_0 = decode(
            freq_1=503,
            freq_2=1009,
            freq_3=2003,
            freq_4=3989,
            samp_rate=samp_rate,
        )
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.decode_0, 3), (self.blocks_null_sink_0, 0))    
        self.connect((self.decode_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.decode_0, 1), (self.qtgui_number_sink_0, 1))    
        self.connect((self.decode_0, 2), (self.qtgui_number_sink_0, 2))    
        self.connect((self.rx_0, 0), (self.decode_0, 0))    
        self.connect((self.tx_0, 0), (self.rx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "system")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.decode_0.set_samp_rate(self.samp_rate)
        self.rx_0.set_samp_rate(self.samp_rate)
        self.tx_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=system, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
