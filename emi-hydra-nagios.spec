Summary: NAGIOS Probe for Hydra Service
Name: emi-hydra-nagios
Version: 1.0.0
Release: 1.noarch
License: Apache Software License
Vendor: EMI
Group: System Environment/Libraries
Packager: ETICS
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: yes
Source: emi-hydra-nagios.tgz

%description
The EMI Hydra Command-line Interface

%prep
 

%setup  

%build
  
  

%install
make install

%clean


%files
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/nagios-plugins-hydra.status
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework//Version.py
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework/__init__.py
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework/AbstractProbe.py
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework/HTTPSHandler.py
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework/Probe.py
/usr/libexec/grid-monitoring/probes/nagios-plugins-hydra/framework/StatusProbe.py

%changelog
 
