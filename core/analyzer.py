import re


def analyzer_log(file_path):
    suspicious_ips = {}
    failed_logins = {}
    forbidden_access = {}
    alerts = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            # extract ip address
            ip_match = re.search(r'(\b(?:\d{1,3}\.){3}\d{1,3}\b)', line)
            if ip_match:
                ip = ip_match.group()
                suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1

                # detect 401 failed login 
                if '401' in line:
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1

                # detect 403 forbidden 
                if '403' in line:
                    forbidden_access[ip] = forbidden_access.get(ip, 0) + 1

        # flag IPs with more than 5 requests
        for ip, count in suspicious_ips.items():
            if count > 5:
                alerts.append({
                    'ip': ip,
                    'count': count,
                    'reason': 'Too many requests'
                })

        # flag IPs with failed logins
        for ip, count in failed_logins.items():
            if count > 0:
                alerts.append({
                    'ip': ip,
                    'count': count,
                    'reason': '❌ Failed Login Attempt (401)'
                })

        # flag IPs with forbidden access
        for ip, count in forbidden_access.items():
            if count > 0:
                alerts.append({
                    'ip': ip,
                    'count': count,
                    'reason': '🚫 Forbidden Access attempted (403)'
                })

    return {
        'total_requests': len(lines),
        'suspicious_ips': suspicious_ips,
        'failed_logins': failed_logins,
        'forbidden_access': forbidden_access,
        'alerts': alerts
    }