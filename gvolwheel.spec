Name:		gvolwheel
Version:	1.0
Release:	%mkrel 1
Summary:	Lightweight application to control the audio volume
License:	GPLv3+
Group:		Sound
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gvolwheel.sourceforge.net/
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-3.0)
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
%__rm -rf %{buildroot}
%makeinstall_std

# remove installed doc, instead use %doc for it
%__rm -rf %{buildroot}%{_usr}/doc

# autostart
%__mkdir_p %{buildroot}%{_sysconfdir}/xdg/autostart
%__cat > %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop << EOF
[Desktop Entry]
Name=GVolWheel
Comment=Lightweight audio volume control application
Comment[ru]=Регулятор громкости
Exec=gvolwheel
Terminal=false
Type=Application
StartupNotify=false
EOF

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_sysconfdir}/xdg/autostart/%{name}.desktop

