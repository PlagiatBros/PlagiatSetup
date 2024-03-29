#! /usr/bin/python3

# ------------------------------------------------------------------------
# ecamonitor: Ecasound monitor client implemented using NetECI
# Copyright (C) 2002-2003,2009 Kai Vehmanen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
# ------------------------------------------------------------------------

import curses
import re
import socket
import string
import sys
import time

ecamonitor_remote_host = "localhost"
ecamonitor_remote_port = 2868
ecamonitor_version     = "v20090419-7"

# TODO:
#  - nothing at the moment

# References:
#  - http://www.python.org/doc/essays/styleguide.html
#  - http://py-howto.sourceforge.net/curses/curses.html
#  - http://www.python.org/doc/2.2.2/lib/module-curses.html
#  - http://py-howto.sourceforge.net/regex/regex.html
#  - http://www.python.org/doc/2.2.2/lib/module-re.html
#  - http://py-howto.sourceforge.net/sockets/sockets.html
#  - http://www.python.org/doc/2.2.2/lib/module-string.html

def connect_to_server(remote_host, remote_port):
    """Connects to the ecasound server.

    @return Socket object for the connection.
    """

    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((remote_host, remote_port))
            s.setblocking(1)
            return(s)

        except Exception as e:
            if e[0] == 111: # 111 = connection refused
                time.sleep(1)
                pass
            else:
                raise

def issue_eiam_command(s, cmd):
    """Sends a command to ecasound and waits for an response.

    @param s socket for an active connection
    @param cmd EIAM command to send

    @return tuple of return value type and value
    """

    tm = ''
    counter = 0
    s.send((cmd + '\r\n').encode())
    while counter < 16:
        count = counter + 1
        newdata = s.recv(16536) # HACK (original: 4096)
        if len(newdata) == 0:
            return ('e','')

        tm = str(tm + newdata.decode())

        # lets test whether we have received a valid
        # EIAM command
        try:
            m = expand_eiam_response(tm)
            return parse_eiam_response(m, tm)

        except Exception as e:
            pass

    return ('e','')

def expand_eiam_response(str):
    """Checks wheter 'str' is a valid EIAM response.

    @return Regex match object.
    """

    m = re.match('256 ([0-9]{1,5}) (.+)\r\n(.*)\r\n\r\n.*', str, re.MULTILINE | re.S)
    return m

def parse_eiam_response(m, str):
    """Parses a valid EIAM response.

    @param m Valid regex match object.
    @param str The whole EIAM response.

    @return tuple of return value type and value
    """

    if not m:
        m = re.match('256 ([0-9]{1,5}) (.+)\r\n(.*)', str, re.MULTILINE | re.S)
        if not m:
            raise Exception('Regexp failed!')

    if m and len(m.groups()) == 0:
        print("(ecamonitor) Matching groups failed: ", m.groups())

    if m and len(m.groups()) == 3:
        #print 'received=', len(m.group(3)), ', expected=', m.group(1)
        if int(m.group(1)) != len(m.group(3)):
            print("(ecamonitor) Response length error.")

    if m:
        return (m.group(2), m.group(3))

    return ('e','')

def main():

    s = None

    remote_host = ecamonitor_remote_host
    remote_port = ecamonitor_remote_port

    if not hasattr(sys, 'hexversion') or sys.hexversion < 0x02070000:
        print('Error! Ecamonitor requires python-2.7, python-3 or newer to run!')
        return 1

    if len(sys.argv) > 1:
        destination = sys.argv[1]
        address = string.split(destination, ':')
        remote_host = address[0]
        if len(address) > 1:
            remote_port = int(address[1])

    try:
        stdscr = curses.initscr()
        pad = curses.newpad(255, 80)
        pad.nodelay(1) # to make getch() nonblocking

        while 1:
            try:
                pad.erase()
                pad.addstr(0, 0, "ecamonitor " + ecamonitor_version, curses.A_BOLD)

                if s == None:
                    pad.addstr(2, 0, "No connection. Trying to connect to " + remote_host + ":" + str(remote_port) + ".\n")
                    pad.refresh(0, 0, 0, 0, stdscr.getmaxyx()[0]-1, stdscr.getmaxyx()[1]-1)
                    #time.sleep(3)
                    s = connect_to_server(remote_host, remote_port)
                    pad.addstr(3, 0, "Connection established.\n")
                    pad.refresh(0, 0, 0, 0, stdscr.getmaxyx()[0]-1, stdscr.getmaxyx()[1]-1)
                    pad.addstr(1, 0, "")
                else:
                    pad.addstr("\n")

                pad.addstr("\n------------------------------------------------------------")
                pad.addstr("\nEngine status: ")
                pad.addstr((issue_eiam_command(s, 'engine-status')[1]), curses.A_BOLD)
                pad.addstr("\nConnected chainsetup: ")
                pad.addstr(issue_eiam_command(s, 'cs-connected')[1], curses.A_BOLD)
                pad.addstr("\nSelected chainsetup: ")
                pad.addstr(issue_eiam_command(s, 'cs-selected')[1], curses.A_BOLD)

                #pad.addstr("\nSelected chainsetup status:: ")
                #pad.addstr(issue_eiam_command(s, 'cs-status')[1])

                pad.addstr("\n\nPosition: ")
                pad.addstr(issue_eiam_command(s, 'cs-get-position')[1] + "s", curses.A_BOLD)
                pad.addstr(" / Length: ")
                pad.addstr(issue_eiam_command(s, 'cs-get-length')[1] + "s", curses.A_BOLD)
                pad.addstr("\nChains: ")
                pad.addstr(str(len(str.split(issue_eiam_command(s, 'c-list')[1],','))), curses.A_BOLD)
                pad.addstr(" / Inputs: ")
                pad.addstr(str(len(str.split(issue_eiam_command(s, 'ai-list')[1],','))), curses.A_BOLD)
                pad.addstr(" / Outputs: ")
                pad.addstr(str(len(str.split(issue_eiam_command(s, 'ao-list')[1],','))), curses.A_BOLD)

                pad.addstr("\n\n------------------------------------------------------------\n")
                res = issue_eiam_command(s, 'aio-status')
                pad.addstr(res[1])

                pad.addstr("\n\n------------------------------------------------------------\n")
                res = issue_eiam_command(s, 'cop-status')
                pad.addstr(res[1])

                pad.addstr("\n\n------------------------------------------------------------\n")
                res = issue_eiam_command(s, 'ctrl-status')
                pad.addstr(res[1])

                pad.addstr("\n\n------------------------------------------------------------\n")

                pad.refresh(0, 0, 0, 0, stdscr.getmaxyx()[0]-1, stdscr.getmaxyx()[1]-1)

                time.sleep(1.0)

                ch=pad.getch()
                if ch == ord('q'):
                    break

            except curses.error:
                raise

            except socket.error as e:
                if e[0] == 32 or e[0] == 104 or e[0] == 111:
                    s = None
                    pass
                else:
                    curses.endwin()
                    print("Exception!" , e)
                    raise

            except KeyboardInterrupt:
                break


    finally:
        if s != None:
            s.close()
        curses.endwin()

if __name__ == '__main__':
    main()
