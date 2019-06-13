@echo off

cd "C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio"
start Ssms.exe

cd "C:\Program Files\Slack"
start Slack.exe

cd "C:\Program Files (x86)\Microsoft Office\root\Office16"
start OUTLOOK.EXE

cd "C:\Program Files (x86)\Google\Chrome\Application"
start chrome.exe /new-tab "http://sysmonweb/SuperMon/#dashboard" "http://odssysmonweb.odsdai.netdai.com/SuperMon/#dashboard" "http://jobscheduler.odshub.com/ProcessStatusDashboard.aspx" "http://jobscheduler.odshub.com/JobSchedulerUtility.aspx?cmpid=1&sort=ID" "http://netmon1/Orion/SummaryView.aspx?viewid=1" "https://my.pingdom.com/3/home"
start chrome.exe /new-tab "https://jira1.daicompanies.com/secure/Dashboard.jspa" "https://confluence1.daicompanies.com/display/ODSPROD/Checklist+Template"
exit