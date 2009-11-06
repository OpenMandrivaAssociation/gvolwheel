Name:		gvolwheel
Version:	0.6
Release:	%mkrel 1
Summary:	Lightweight application to control the audio volume
License:	GPLv3+
Group:		Sound
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gvolwheel.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	intltool

%description
GVolWheel is application which lets you control the volume easily
through a tray icon you can scroll on. Easily integrate with minimal
desktops (Openbox,IceWM,XFCE etc).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

# remove installed doc, instead use %doc for it
rm -rf %{buildroot}%{_usr}/doc

# autostart
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cat > %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop << EOF
[Desktop Entry]
Name=GVolWheel
Comment=Lightweight audio volume control application
Exec=gvolwheel
Terminal=false
Type=Application
StartupNotify=false
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING ChangeLog INSTALL README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop


