#!/usr/bin/python


import platform, os, commands


def distribution_detect():
        # https://en.wikipedia.org/wiki/List_of_Linux_distributions

        releases = {

                # RPM bases
                'Red Hat'       : ['/etc/redhat-release',],
                'CentOS'        : ['/etc/centos-release',],
                'Fedora Core'   : ['/etc/fedora-release',],
                'SuSE'          : ['/etc/SuSE-release', '/etc/suse-release'],
                'Mandrake Linux': ['/etc/mandrake-release','/etc/mandakelinux-release'],

                # CentOS/RHEL-based
                'Asianux'       : [],
                'ClearOS'       : [],
                'Fermi Linux LTS':[],
                'Miracle Linux' : [],
                'Oracle Linux'  : [],
                'Red Flag Linux': [],
                'Rocks Cluster Distribution':[],
                'Scientific Linux':[],
                'SME Server'    : ['/etc/e-smith-release',],

                # Fedora-based
                'Aurora SPARC Linux':[],
                'Berry Linux'   : [],
                'BLAG Linux and GNU':[],
                'EduLinux'      : [],
                'EnGarde Secure Linux':[],
                'Fuduntu'       : [],
                'Hanthana'      : [],
                'K12LTSP'       : [],
                'Korora'        : [],
                'Linpus Linux'  : [],
                'MeeGo'         : [],
                'Moblin'        : [],
                'MythDora'      : [],
                'Network Security Toolkit'
                'Ojuba Linux'   : [],
                'Qubes OS'      : [],
                'Russian Fedora Remix'
                'Sugar-on-a-Stick Linux'
                'Trustix'       : [],
                'Yellow Dog'    : ['/etc/yellowdog-release',],

                # openSUSE-based
                'SUSE Linux Enterprise Desktop'
                'SUSE Linux Enterprise Server': ['/etc/sles-release',],
                'SUSE Studio'   : [],

                # urpmi-based
                'Mandriva Linux': ['/etc/mandriva-release',],
                'Mageia'        : [],
                'ROSA Linux'    : [],
                'OpenMandriva'  : [],
                'Annvix'        : ['/etc/annvix-release',],
                'TinyMe'        : [],
                'Trinity Rescue Kit':[],
                'Unity Linux'   : [],

                # apt-rpm based
                'PCLinuxOS'     : [],
                'Vine Linux'    : [],
                'ALT Linux'     : [],

                # Independent RPM distributions
                'Caldera OpenLinux':[],
                'cAos Linux'    : [],
                'TurboLinux'    : ['/etc/turbolinux-release'],
                'YOPER'

                # Debian base
                'Debian'        : ['/etc/debian_version',],
                'LinuxBBQ'      : [],
                'Ubuntu'        : [],
                'Kali Linux'    : [],
                'Parsix'        : [],
                'BackTrack'     : [],
                'Edubuntu'      : [],
                'Kubuntu'       : [],

                'United Linux'  : ['/etc/UnitedLinux-release',],
                'Arch Linux'    : ['/etc/arch-release',],
                'Arklinux'      : ['/etc/arklinux-release',],
                'Aurox Linux'   : ['/etc/aurox-release',],
                'BlackCat'      : ['/etc/blackcat-release',],
                'Cobalt'        : ['/etc/cobalt-release',],
                'Conectiva'     : ['/etc/conectiva-release',],
                'Debian'        : ['/etc/debian_version',],
                'Gentoo Linux'  : ['/etc/gentoo-release',],
                'Immunix'       : ['/etc/immunix-release',],
                'Knoppix'       : ['/etc/knoppix_version',],
                'Linux-From-Scratch':['/etc/lfs-release',],
                'Linux-PPC'     : ['/etc/linuxppc-release',],
                'MkLinux'       : ['/etc/mklinux-release',],
                'Novell Linux Desktop':['/etc/nld-release',],
                'PLD Linux'     : ['/etc/pld-release',],
                'Slackware'     : ['/etc/slackware-version',],
                'Solaris SPARC' : ['/etc/release',],
                'Sun JDS'       : ['/etc/sun-release',],
                'Tiny Sofa'     : ['/etc/tinysofa-release',],
                'UltraPenguin'  : ['/etc/ultrapenguin-release',],
                'VA-Linux/RH-VALE':['/etc/va-release',],
        }

        ret = {}
        for name in releases:
                for filename in releases[name]:
                        if os.path.isfile( filename ):
                                ret[ 'release' ] = open( filename ).read()

        if not os.path.isfile( '/usr/bin/lsb_release' ):
                return ret

        lsbDict = {
                'i'     : 'distribution'        ,
                'd'     : 'release'             ,
                'r'     : 'releaseVersion'      ,
                'c'     : 'releaseName'         ,
        }
        for lsbKey in lsbDict:
                ret[ lsbDict[lsbKey] ] = \
                        commands.getoutput( '/usr/bin/lsb_release -%s' % lsbKey ).split(':')[-1].strip()

        return ret


def system_detect():

        # platform uname
        uname   = platform.uname()
        system  = uname[0]
        node    = uname[1]
        release = uname[2]
        version = uname[3]
        machine = uname[4]
        processor=uname[5]

        ret = {
                'system'                : system        ,
                'node'                  : node          ,
                'release'               : release       ,
                'systemVersion'         : version       ,
                'systemMachine'         : machine       ,
                'systemProcessor'       : processor     ,
        }

        dist = distribution_detect()
        for release in dist:
                ret[ release ] = dist[ release ]


        return ret


if __name__ == '__main__':

        import pprint

        print "distribution detect:"
        pprint.pprint( distribution_detect() )
        print

        print "system detect:"
        pprint.pprint( system_detect() )
        print

