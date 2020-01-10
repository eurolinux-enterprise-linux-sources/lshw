Summary:       HardWare LiSter
Name:          lshw
Version:       B.02.18
Release:       7%{?dist}
License:       GPLv2
Group:         Applications/System
URL:           http://ezix.org/project/wiki/HardwareLiSter
Source0:       http://www.ezix.org/software/files/%{name}-%{version}.tar.gz
Source1:       lshw.desktop
Source2:       org.ezix.lshw.gui.policy
Source3:       lshw-gui
Patch0:        0001-release-clean-up.patch
Patch1:        0002-fix-tar-archive-to-avoid-spilling-.spec-file-outside.patch
Patch2:        0003-update-.gitignore.patch
Patch3:        0004-add-bug-reporting-URL.patch
Patch4:        0005-update-doc.patch
Patch5:        0006-fix-714-system-width-detection.patch
Patch6:        0007-update-data-files.patch
Patch7:        0008-Makefile-allow-to-pass-additional-LIBS.patch
Patch8:        0009-add-install-instructions.patch
Patch9:        0010-fix-716-crash-in-scan_dmi_sysfs-when-run-as-non-root.patch
Patch10:       0011-report-modalias-information-for-PCI-and-network-devi.patch
Patch11:       0012-code-clean-up-only-set-businfo-or-modalias-when-it-s.patch
Patch12:       0013-make-modalias-an-optional-attribute-only-reported-in.patch
Patch13:       0014-add-detection-of-VirtualBox-disks.patch
Patch14:       0015-osutils-Using-delete-instead-of-delete.patch
Patch15:       0016-pci-Adjusting-visual-alignment-of-const-values.patch
Patch16:       0017-merge-Github-pull-request-22.patch
Patch17:       0018-merge-github-pull-request-23-parse-CPU-information.patch
Patch18:       0019-fix-727-GUI-build-issue-with-SQLite.patch
Patch19:       0020-devtree-Display-CPU-nodes-before-memory.patch
Patch20:       0021-devtree-Add-machine-description.patch
Patch21:       0022-devtree-Fix-motherboard-model-reporting.patch
Patch22:       0023-devtree-Fix-physical-ID-info-for-CPU-nodes.patch
Patch23:       0024-devtree-Add-VPD-info-for-FSP-based-Power-System.patch
Patch24:       0025-devtree-Add-VPD-info-for-BMC-based-IBM-Power-System.patch
Patch25:       0026-cpuinfo-Rectify-cpuinfo-for-IBM-Power-Systems.patch
Patch26:       0027-devtree-Add-parsed-firmware-version-info.patch
Patch27:       0028-devtree-Add-add_device_tree_info.patch
Patch28:       0029-pci-Add-device-tree-info.patch
Patch29:       0030-Fix-typo-classes-when-checking-if-temp-sysfs-got-mou.patch
Patch30:       0031-Adding-json-option-in-help-output.patch
Patch31:       0032-devtree-Use-consistent-output-format.patch
Patch32:       0033-devtree-Code-cleanup.patch
Patch33:       0034-devtree-Refactor-SPD-handling-code.patch
Patch34:       0035-devtree-Don-t-overrun-dimminfo-buffer.patch
Patch35:       0036-devtree-Add-description-vendor-and-clock-info-to-mem.patch
Patch36:       0037-devtree-Add-part-and-serial-number-info-to-memory-ba.patch
Patch37:       0038-devtree-Report-memory-info-for-BMC-based-Power-Syste.patch
Patch38:       0039-devtree-Correctly-read-size-for-DDR4-SPD.patch
Patch39:       0040-devtree-Add-support-for-DDR4-SPD.patch
Patch40:       0041-osutils-don-t-segfault-on-empty-files.patch
Patch41:       0042-Add-forgetten-size-checks-when-using-loadfile.patch
Patch42:       0043-fix-741-Detect-disk-vendor-SimpleTech.patch
Patch43:       0001-output-pci-subsystem-information-611.patch
Patch44:       0002-also-output-subsystem-info-for-PCI-host-bridges-611.patch
Patch45:       0003-only-output-subsystem-info-if-the-ids-are-non-zero-6.patch
Patch46:       0004-improve-model-and-chassis-retrieval-for-IBM-systems-.patch
Patch47:       0005-detect-arch-at-runtime-for-proc-cpuinfo-parsing.patch
Patch48:       0007-add-missing-PCI-storage-subclasses-688.patch
Patch49:       0008-expose-hints-in-XML-output-688.patch
Patch50:       0011-scan-PnP-devices-in-sysfs-691.patch
Patch51:       0012-load-PnP-vendor-names-from-hwdata-database-691.patch
Patch52:       0013-load-PnP-product-names-from-Universit-t-Regensburg-p.patch
Patch53:       0014-add-a-few-missing-PnP-IDs.patch
Patch54:       0015-scan-vio-devices-in-sysfs-692.patch
Patch55:       0016-use-sysfs-to-find-businfo-for-SCSI-adapters-692.patch
Patch56:       0017-scan-S-390-devices-in-sysfs-693.patch
Patch57:       0018-guess-memory-size-from-memory-hotplug-info-694.patch
Patch58:       0019-devicetree-identify-DIMMs-from-IBM-memory-controller.patch
Patch59:       0022-dmi-x86-64-is-a-misnomer-for-64-bit-CPU-capability-6.patch
Patch60:       0023-dmi-avoid-creating-multiple-memory-nodes-700.patch
Patch61:       0025-scsi-initialize-parent-inside-the-loop-692.patch
Patch62:       0026-sysfs-businfo-for-USB-devices-692.patch
Patch63:       0001-lshw-Parse-OPAL-firmware-properties-from-the-device-.patch
Patch64:       0001-Add-a-new-element-vendor_id.patch
Patch65:       0001-Revert-better-handling-of-whole-disk-volumes.patch
Patch66:       0001-Proper-detect-vendor_id-device_id-for-virtual-functi.patch
Patch67:       0001-Show-right-version-number.patch

BuildRequires: sqlite-devel
Requires:      hwdata

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton on
the hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86s
systems and on some PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://lshw.ezix.org/

%package       gui
Summary:       HardWare LiSter (GUI version)
Group:         Applications/System
Requires:      polkit
Requires:      %{name} >= %{version}
Requires:      gtk2 >= 2.4
BuildRequires: gtk2-devel >= 2.4
BuildRequires: desktop-file-utils

%description gui
lshw (Hardware Lister) is a small tool to provide detailed informaton on
the hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86s
 systems and on some PowerPC machines (PowerMac G4 is known to work).

This package provides a graphical user interface to display hardware
information.

For detailed information on lshw features and usage, please see the
included documentation or go to the lshw Web page,
http://lshw.ezix.org/

%prep
%setup -q
%patch0 -p1
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
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1

%build
make %{?_smp_mflags} SBINDIR="%{_sbindir}" RPM_OPT_FLAGS="%{optflags}" SQLITE=1 gui

# Replace copyrighted icons
pushd src
make nologo

%install
make install                   \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        STRIP="/bin/true"      \
        INSTALL="install -p"   \
        SQLITE=1

make install-gui               \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        STRIP="/bin/true"      \
        INSTALL="install -p"   \
        SQLITE=1

ln -s -f gtk-lshw %{buildroot}%{_sbindir}/lshw-gui

# don't package these copies, use the ones from hwdata instead
rm -f %{buildroot}%{_datadir}/%{name}/pci.ids
rm -f %{buildroot}%{_datadir}/%{name}/usb.ids
# don't package these copies, they're not actually used by the app,
# and even if they were, should use the hwdata versions
rm -f %{buildroot}%{_datadir}/%{name}/oui.txt
rm -f %{buildroot}%{_datadir}/%{name}/manuf.txt

# desktop icon
install -D -m 0644 -p ./src/gui/artwork/logo.svg \
     %{buildroot}%{_datadir}/pixmaps/%{name}-logo.svg
desktop-file-install %{?vendortag:--vendor fedora} \
  --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# PolicyKit
install -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
install -D -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/lshw-gui

# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/fr/

#files -f %{name}.lang
%files
%license COPYING
%doc README.md docs/*
%{_mandir}/man1/lshw.1*
%{_sbindir}/%{name}

%files gui
%{_bindir}/%{name}-gui
%{_sbindir}/gtk-%{name}
%{_sbindir}/%{name}-gui
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-logo.svg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy

%changelog
* Tue May 16 2017 Petr Oros <poros@redhat.com> - B.02.18-7
- Revert Fix JSON output format
- Show right version number
- Resolves: #1447761

* Fri May 5 2017 Petr Oros <poros@redhat.com> - B.02.18-6
- Fix JSON output format
- Resolves: #1205372

* Wed May 3 2017 Petr Oros <poros@redhat.com> - B.02.18-5
- Re-enable sqlite support (for -dump)
- Resolves: #1446761

* Fri Mar 17 2017 Petr Oros <poros@redhat.com> - B.02.18-4
- Fix tmp_device_id/tmp_vendor_id size
- Resolves: #1339378

* Fri Mar 17 2017 Petr Oros <poros@redhat.com> - B.02.18-3
- Proper detect vendor_id/device_id for virtual functions
- Resolves: #1339378

* Tue Mar 7 2017 Petr Oros <poros@redhat.com> - B.02.18-2
- Add missing doc files
- Resolves: #1368704

* Fri Mar 3 2017 Petr Oros <poros@redhat.com> - B.02.18-1
- Rebase to lshw-B.02.18
- Sync with upstream git
- Apply patches from beaker-fork
- Resolves: #1368704

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
