# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 NovaPoint Group LLC (<http://www.novapointgroup.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
{
    'name': 'Assign/Unassign Followers',
    'version': '1.1',
    'category': 'Settings',
    'description': """
    Assign or Unassign Followers to a record for any model
    * After Installed the module go to->Settings-> Technical-> Actions
    * Under the Actions -> Assign/Unassign Followers where you can able to create the followers
    * Create add name and model then click the Add Action button
    * Go to relevant model menu and select records in list view then assign the followers using "More" menu.
""",
    #'price': 22.00,
   # 'currency': 'EUR',
    'author': 'MAGESH',
    'depends': ['base'],
    'init_xml': [],
    'update_xml': ["assign_followers_view.xml"],
    'demo_xml': [],
    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
