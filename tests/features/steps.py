# coding=utf-8
from lettuce import step, world
from areafigura import AreaFigura

# -----------------------------------------------------------------------------
# ---------------------------------- Figuras ----------------------------------
# -----------------------------------------------------------------------------
@step(u'Dado que ingreso los datos necesarios')
def dado_que_ingreso_los_datos_necesarios(step):
    world.figura = AreaFigura()


@step(u'cuando quiero calcular el área de un rectángulo con base de "([^"]*)" y altura de "([^"]*)"')
def cuando_quiero_calcular_el_area_de_un_rectangulo_con_base_de_group1_y_altura_de_group2(step, base, altura):
    world.figura.area_rectangulo(float(base), float(altura))


@step(u'cuando quiero calcular el área de un cuadrado con lado de "([^"]*)"')
def cuando_quiero_calcular_el_area_de_un_cuadrado_con_lado_de_group1(step, lado):
    world.figura.area_cuadrado(float(lado))


@step(u'cuando quiero calcular el área de un círculo con radio de "([^"]*)"')
def cuando_quiero_calcular_el_area_de_un_circulo_con_radio_de_group1(step, radio):
    world.figura.area_circulo(float(radio))


@step(u'cuando quiero calcular el área de un trapecio con base mayor de "([^"]*)", base menor de "([^"]*)" y altura de "([^"]*)"')
def cuando_quiero_calcular_el_area_de_un_trapecio_con_base_mayor_de_group1_base_menor_de_group2_y_altura_de_group2(step, base_mayor, base_menor, altura):
    world.figura.area_trapecio(float(base_mayor), float(base_menor), float(altura))


@step(u'entonces obtengo un área de "([^"]*)"')
def entonces_obtengo_un_area_de_group1(step, esperado):
    obtenido = world.figura.get_area()
    assert float(esperado) == float(obtenido), \
        'El resultado esperado es: ' + esperado + \
        " y el obtenido es: " + str(obtenido)
