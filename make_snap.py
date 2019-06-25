#!/usr/bin/env python

import os
import re

class Color:
  RED     ='\033[1;31m'
  GREEN   ='\033[1;32m'
  YELLOW  ='\033[1;33m'
  BLUE    ='\033[1;34m'
  MAGENTA ='\033[1;35m'
  CYAN    ='\033[1;36m'
  WHITE   ='\033[0;37m'
  END     ='\033[0m'
  KO = RED   + 'KO' + END
  OK = GREEN + 'OK' + END

# --------------------------------------------------
if __name__ == '__main__':
    os.unsetenv ('http_proxy')
    os.unsetenv ('https_proxy')

    with open ('../5.0/sources/BellePoule/application/version.h') as version_file:
        for line in version_file:
            if 'VERSION_MATURITY' in line:
                version = line.split ('"')

                with open ('snapcraft.template', 'r') as template:
                    with open ('snapcraft.yaml', 'w') as yaml:
                        content = re.sub (r'__VERSION', version[1], template.read ())
                        yaml.write (content)

                break

    print 'sudo snapcraft --debug'
    print 'sudo snap install --devmode bellepoulebeta_5.0' + version[1] + '_amd64.snap'
