Summary:       Hardware lister
Name:          lshw
Version:       B.02.17
Release:       12%{?dist}
License:       GPLv2
Group:         Applications/System
URL:           http://ezix.org/project/wiki/HardwareLiSter
Source0:       http://www.ezix.org/software/files/lshw-%{version}.tar.gz
Source1:       lshw.desktop
Source2:       org.ezix.lshw.gui.policy
Source3:       lshw-gui
Patch0:        lshw-B.02.17-scan-fat-mem-bug.patch
Patch1:        no_smbios_unsupp.patch
Patch2:        0001-IBM-PowerNV.patch
Patch3:        0002-IBM-PowerNV.patch
Patch4:        0003-IBM-PowerNV.patch
Patch5:        0004-IBM-PowerNV.patch
Patch6:        0001-use-sysfs-for-DMI-info-when-available-696-666-664.patch
Patch7:        0dff3470.patch
Patch8:        0001-Add-pseries-guest-information-711.patch
Patch9:        0001-lshw-Parse-OPAL-firmware-properties-from-the-device-.patch
Patch10:       0001-add-S-390-specific-CPU-info.patch
Patch11:       0001-Retrieving-CPU-Information-on-IBM-s390x-and-ARM-syst.patch
Patch12:       0001-assume-we-have-an-SMP-capable-systems-whenever-sever.patch
Patch13:       0001-fix-S-390-compilation.patch
Patch14:       0001-add-missing-PCI-storage-subclasses-688.patch
Patch15:       0002-expose-hints-in-XML-output-688.patch
Patch16:       0003-refactored-sysfs-entry-to-always-store-resolved-devi.patch
Patch17:       0004-scan-virtio-devices-in-sysfs-562.patch
Patch18:       0001-scan-vio-devices-in-sysfs-692.patch
Patch19:       0002-use-sysfs-to-find-businfo-for-SCSI-adapters-692.patch
Patch20:       0001-Add-missing-sysfs-entry-string_attr.patch
Patch21:       0001-Revert-better-handling-of-whole-disk-volumes.patch

BuildRequires: sqlite-devel
Requires:      hwdata

%description
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems and on some
PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%package       gui
Summary:       Graphical hardware lister
Group:         Applications/System
Requires:      polkit
Requires:      %{name} = %{version}-%{release}
BuildRequires: gtk2-devel >= 2.4
BuildRequires: desktop-file-utils

%description   gui
Graphical frontend for the hardware lister (lshw) tool.
If desired, hardware information can be saved to file in
plain, XML or HTML format.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

%build
%{__make} %{?_smp_mflags} SBINDIR="%{_sbindir}" RPM_OPT_FLAGS="%{optflags}" SQLITE=1 gui 

# Replace copyrighted icons
pushd src
%{__make} nologo

%install
%{__make} install              \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        SQLITE=1               \
        STRIP="/bin/true"      \
        INSTALL="%{__install} -p"

%{__make} install-gui          \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        SQLITE=1               \
        STRIP="/bin/true"      \
        INSTALL="%{__install} -p"

%{__ln_s} -f gtk-lshw %{buildroot}%{_sbindir}/lshw-gui

# don't package these copies, use the ones from hwdata instead
%{__rm} -f %{buildroot}%{_datadir}/%{name}/pci.ids
%{__rm} -f %{buildroot}%{_datadir}/%{name}/usb.ids
# don't package these copies, they're not actually used by the app,
# and even if they were, should use the hwdata versions
%{__rm} -f %{buildroot}%{_datadir}/%{name}/oui.txt
%{__rm} -f %{buildroot}%{_datadir}/%{name}/manuf.txt

# desktop icon
%{__install} -D -m 0644 -p ./src/gui/artwork/logo.svg \
     %{buildroot}%{_datadir}/pixmaps/%{name}-logo.svg
desktop-file-install %{?vendortag:--vendor fedora} \
  --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# PolicyKit
%{__install} -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
%{__install} -D -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/lshw-gui

# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/fr/

#files -f %{name}.lang
%files
%doc COPYING README docs/*
%doc %{_mandir}/man1/lshw.1*
%{_sbindir}/%{name}

%files gui
%doc COPYING
%{_bindir}/%{name}-gui
%{_sbindir}/gtk-%{name}
%{_sbindir}/%{name}-gui
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-logo.svg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy

%changelog
* Mon Aug 8 2016 Petr Oros <poros@redhat.com> - B.02.17-12
- Revert: "better" handling of whole-disk volumes
- Resolves: #1358748

* Mon Aug 1 2016 Petr Oros <poros@redhat.com> - B.02.17-11
- Resolves: #1360662

* Tue Jul 26 2016 Petr Oros <poros@redhat.com> - B.02.17-10
- Add support for reporting virtio devices
- Resolves: #1360662

* Mon Jul 25 2016 Petr Oros <poros@redhat.com> - B.02.17-9
- Add support for proper report cpuinfo on s390x arch
- Resolves: #1208276

* Tue Jun 7 2016 Petr Oros <poros@redhat.com> - B.02.17-8
- Add pseries-guest information and PowerNV-firmware information
- Resolves: #1334603

* Fri Apr 29 2016 Petr Oros <poros@redhat.com> - B.02.17-7
- Report the vendor_id field for x86 cpu's
- Resolves: #1215245

* Mon Jan 25 2016 Petr Oros <poros@redhat.com> - B.02.17-6
- Use sysfs for DMI info when available
- Resolves: #1261570

* Mon Sep 14 2015 Petr Oros <poros@redhat.com> - B.02.17-5
- Resolves: #1221933
- Remove Trailing newline in 0004-IBM-PowerNV.patch

* Tue Jun 30 2015 Petr Oros <poros@redhat.com> - B.02.17-4
- Resolves: #1221933
- Fix malformed patch for PowerNV/bare-metal

* Tue Jun 30 2015 Petr Oros <poros@redhat.com> - B.02.17-3
- Resolves: #1221933
- Add power specific patches to RHEL7.2 for PowerNV/bare-metal

* Mon Dec 15 2014 Petr Oros <poros@redhat.com> - B.02.17-2
- Resolves: #1174195
- Don't look for SMBIOS structures on PowerPC and s390x systems

* Mon Nov 3 2014 Petr Oros <poros@redhat.com> - B.02.17-1
- Resolves: #1101590
- Initial package.
