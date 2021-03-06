#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
import datetime

STATUS = [
    ('1', 'Esboco'),
    ('2', 'Visualizado'),
    ('3', 'Atendimento'),
    ('4', 'Corrigido'),
    ('5', 'Cancelado')]

CRITICIDADE = [
    ('1', 'BAIXA'),
    ('2', 'MEDIA'),
    ('3', 'ALTA'),
]


class Ocorrencias(osv.Model):
    _name = 'ocorrencia'
    _columns = {
        'ocorrencia_titulo': fields.char('Titulo'),
        'ocorrencia_descricao': fields.text('Descricao'),
        'state': fields.selection(selection=STATUS, string='Status', size=2,
                                  track_visibility='onchange'),
        'ocorrencia_foto': fields.binary('Foto'),
        'ocorrencia_mapa': fields.binary('Mapa'),
        'ocorrencia_longitude': fields.char('Longitude'),
        'ocorrencia_latitude': fields.char('latitude'),
        'ocorrencia_descricao_complementar': fields.text('Outras descricoes'),
        'ocorrencia_endereco_aproximado': fields.char('Endereco aproximado', readonly=True),
        'ocorrencia_criticidade': fields.selection(selection=CRITICIDADE, string='Criticidade',
                                                   size=2, track_visibility='onchange'),
        'ocorrencia_data': fields.date(string='Data'),
        #__M2O__
        'funcionario_id': fields.many2one('funcionario', 'Funcionario'),

    }

    _defaults = {
        'state': '1',
    }