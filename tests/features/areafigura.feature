Feature: Área de una figura
	Como usuario de la calculadora de área de figuras geométricas
	deseo ingresar los datos necesarios
    para calcular el área de una figura determinada de manera precisa

	Scenario: Área de un rectángulo con base de 5 y altura de 6
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un rectángulo con base de "5" y altura de "6"
		entonces obtengo un área de "30"

    Scenario: Área de un rectángulo con base de 10 y altura de 4.5
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un rectángulo con base de "10" y altura de "4.5"
		entonces obtengo un área de "45"

    Scenario: Área de un cuadrado con lado de 12
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un cuadrado con lado de "12"
		entonces obtengo un área de "144"

    Scenario: Área de un cuadrado con lado de 10
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un cuadrado con lado de "10"
		entonces obtengo un área de "100"

    Scenario: Área de un círculo con radio de 10
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un círculo con radio de "10"
		entonces obtengo un área de "314.16"

    Scenario: Área de un círculo con radio de 33
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un círculo con radio de "33"
		entonces obtengo un área de "3421.20"

    Scenario: Área de un trapecio con base mayor de 6, base menor de 5 y altura de 5
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un trapecio con base mayor de "6", base menor de "5" y altura de "5"
		entonces obtengo un área de "27.5"

    Scenario: Área de un trapecio con base mayor de 8, base menor de 3 y altura de 4
		Dado que ingreso los datos necesarios
		cuando quiero calcular el área de un trapecio con base mayor de "8", base menor de "3" y altura de "4"
		entonces obtengo un área de "22"
