# https://github.com/nilcons/libpam-python-pgsql/

import sys
sys.path += [ '/usr/lib/python2.7/dist-packages' ]
from pg import DB

# TODO: implement some aggregated successful/failed login attempt statistics gathering into the postgres database

def pam_sm_authenticate(pamh, flags, argv):
    # try:
    #   user = pamh.get_user(None)
    # except pamh.exception as e:
    #   return e.pam_result
    # return pamh.PAM_AUTH_ERR
    vars = {}
    for i in argv:
        where = i.find('=')
        if where > 0:
            vars[i[:where]] = i[where+1:]
    try:
        # svc = pamh.service
        # print("SVC: " + svc)
        user = pamh.get_user(None)
        pwd = pamh.authtok
        db = DB(dbname = vars['db'], user = vars['dbuser'])
        res = db.query("SELECT COUNT(1) FROM " + vars['table'] +
                            " WHERE " + vars['usercolumn'] + " = $1 AND "
                            + vars['pwdcolumn'] + " = $2",
                            user, pwd)
        count = res.getresult()[0][0]
        db.close()
        # print("RESULT", count)
        if count > 0:
            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_AUTH_ERR
    except Exception as e:
        # print(e)
        return pamh.PAM_AUTH_ERR
    return pamh.PAM_AUTH_ERR
