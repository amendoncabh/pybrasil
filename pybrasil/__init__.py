# -*- coding: utf-8 -*-

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)


from . import (base, certificado, codigo_barras, data, febraban, feriado, ibge, inscricao, ncm, produto, telefone,
               template, valor, webservice)
from .python_pt_BR import python_pt_BR

import sys
import locale

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    locale.setlocale(locale.LC_ALL, b'pt_BR.UTF-8')
    locale.setlocale(locale.LC_COLLATE, b'pt_BR.UTF-8')

else:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
