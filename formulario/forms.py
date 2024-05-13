from django import forms

class FormularioForm(forms.Form):
    apellido_paterno = forms.CharField(label='Apellido Paterno', max_length=100)
    apellido_materno = forms.CharField(label='Apellido Materno', max_length=100)
    nombres = forms.CharField(label='Nombres', max_length=100)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', input_formats=['%d/%m/%Y'])
    email_personal = forms.EmailField(label='Email Personal')
    telefono_celular = forms.CharField(label='Teléfono Celular', max_length=15)
    mes_y_anio_egreso = forms.CharField(label='Mes y Año de Egreso', max_length=100)
    calidad_docentes = forms.ChoiceField(
        label='Calidad de los docentes',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    plan_estudios = forms.ChoiceField(
        label='Plan de estudios',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    oportunidad_investigacion = forms.ChoiceField(
        label='Oportunidad de participar en proyectos de investigación y desarrollo',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    satisfaccion_condiciones_estudio = forms.ChoiceField(
        label='Satisfacción de las condiciones de estudio (infraestructural)',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    actividad_actual = forms.ChoiceField(
        label='Actividad a la que se dedica actualmente',
        choices=[
            ('trabaja', 'Trabaja'),
            ('estudia', 'Estudia'),
            ('estudia_y_trabaja', 'Estudia y trabaja'),
            ('ni_estudia_ni_trabaja', 'No estudia ni trabaja'),
        ],
        widget=forms.RadioSelect
    )
    
    trabajo_tics = forms.ChoiceField(
        label='Si está trabajando, su trabajo está relacionado con el área de Tics',
        choices=[
            ('si', 'Sí'),
            ('no', 'No'),
        ],
        widget=forms.RadioSelect
    )
    
    razon_social = forms.CharField(label='Razón Social', max_length=100)
    domicilio = forms.CharField(label='Domicilio', max_length=100)
    calle_numero = forms.CharField(label='Calle y Número', max_length=100)
    colonia_cp_ciudad = forms.CharField(label='Colonia, C.P., Ciudad', max_length=100)
    municipio = forms.CharField(label='Municipio', max_length=100)
    estado = forms.CharField(label='Estado', max_length=100)
    telefonos = forms.CharField(label='Teléfonos', max_length=100)
    jefe_inmediato = forms.CharField(label='Nombre y Puesto del Jefe Inmediato', max_length=100)
    
    eficiencia_laboral = forms.ChoiceField(
        label='Eficiencia para realizar las actividades laborales, en relación a su formación académica',
        choices=[
            ('muy_eficiente', 'Muy eficiente'),
            ('eficiente', 'Eficiente'),
            ('poco_eficiente', 'Poco eficiente'),
            ('deficiente', 'Deficiente'),
        ],
        widget=forms.RadioSelect
    )

    calificacion_formacion_laboral = forms.ChoiceField(
        label='Cómo califica su formación académica con respecto a su desempeño laboral',
        choices=[
            ('excelente', 'Excelente'),
            ('bueno', 'Bueno'),
            ('regular', 'Regular'),
            ('malo', 'Malo'),
            ('pesimo', 'Pésimo'),
        ],
        widget=forms.RadioSelect
    )

    utilidad_residencias_practicas = forms.ChoiceField(
        label='Utilidad de las residencias profesionales o prácticas profesionales para su desarrollo laboral y profesional',
        choices=[
            ('excelente', 'Excelente'),
            ('bueno', 'Bueno'),
            ('regular', 'Regular'),
            ('malo', 'Malo'),
            ('pesimo', 'Pésimo'),
        ],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_area_estudio = forms.ChoiceField(
        label='Área o campo de estudio',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_titulacion = forms.ChoiceField(
        label='Titulación',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_experiencia_laboral = forms.ChoiceField(
        label='Experiencia laboral/práctica (antes de egresar)',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_competencia_laboral = forms.ChoiceField(
        label='Competencia Laboral',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_posicionamiento_institucion = forms.ChoiceField(
        label='Posicionamiento de la Institución de Egreso',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_conocimiento_idiomas = forms.ChoiceField(
        label='Conocimiento de Idiomas Extranjeros',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_recomendaciones_referencias = forms.ChoiceField(
        label='Recomendaciones/referencias',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_personalidad_actitudes = forms.ChoiceField(
        label='Personalidad/actitudes',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_capacidad_liderazgo = forms.ChoiceField(
        label='Capacidad de liderazgo',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    aspectos_valora_empresa_otros = forms.ChoiceField(
        label='Otros',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    
    compromiso_nivel_compromiso_trabajo = forms.ChoiceField(
        label='Manifiesta un alto nivel de compromiso en el trabajo personal y del departamento, además de ser puntual y desarrollar su trabajo con un alto nivel de calidad.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    compromiso_sentimiento_afinidad = forms.ChoiceField(
        label='Maneja un alto sentimiento de afinidad y fidelidad hacia la organización para la que labora.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    compromiso_desarrollo_capacidades = forms.ChoiceField(
        label='En su trabajo desarrolla sus capacidades y aprende nuevas capacidades.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    compromiso_aporte_profesional = forms.ChoiceField(
        label='Sirve y aporta profesionalmente a favor de enaltecer su persona y el de la institución.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    compromiso_iniciativa_resolucion_problemas = forms.ChoiceField(
        label='Manifiesta iniciativa para resolver los problemas surgidos en el desempeño de su trabajo o en el de la empresa para la que labora.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )


    responsabilidad_trabajo_completo = forms.ChoiceField(
        label='Realiza sus funciones con la certeza de que su trabajo está completo y bien hecho a la primera vez y siempre.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    responsabilidad_puntualidad_entrega = forms.ChoiceField(
        label='Tiene por costumbre llegar y entregar en el tiempo acordado a sus compromisos y obligaciones.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    responsabilidad_normatividad = forms.ChoiceField(
        label='Realiza sus funciones apegado a la normatividad considerando el desarrollo de métodos eficientes, estableciendo metas y objetivos, así como el logro de ellos.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    
    honestidad_concordancia_ideas_acciones = forms.ChoiceField(
        label='Maneja un alto nivel de concordancia entre sus ideas y sus acciones apegado a lo que se considera normal dentro de la empresa.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    honestidad_expresion_ideas_opiniones = forms.ChoiceField(
        label='Expresa sus ideas y opiniones teniendo en cuenta las emociones de su interlocutor.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    honestidad_carta_referencia = forms.ChoiceField(
        label='Un gran amigo, que está buscando trabajo hace tiempo, te pide que escribas una referencia para un trabajo que consideras no está preparado. ¿Le escribes la carta de referencia?',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    
    
    competencia_diseno_configuracion_redes = forms.ChoiceField(
        label='Cuenta con la competencia para diseñar y configurar redes LAN y WAN, siguiendo normas y estándares vigentes.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    competencia_administracion_seguridad_redes = forms.ChoiceField(
        label='Cuenta con la competencia para administrar, establecer niveles de seguridad y escalar redes LAN y WAN.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    
    
    competencia_analizar_disenar_programar = forms.ChoiceField(
        label='Establezca cual es su nivel de competencia para analizar, diseñar, programar y documentar, siguiendo estándares, con algún lenguaje específico como Java, JavaScript, C, Python, o algún otro.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    competencia_desarrollar_sistemas_web = forms.ChoiceField(
        label='Determine su nivel de competencia al analizar, diseñar y desarrollar sistemas web, siguiendo estándares, con algún lenguaje específico como PHP, HTML5, ASP.NET, Ruby o algún otro.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    competencia_programar_dispositivos_moviles = forms.ChoiceField(
        label='Cuenta con la competencia de analizar, diseñar y programar dispositivos móviles, siguiendo estándares, con alguna plataforma específica como Android, IOS, Movil App Development, Xmarin Studio, PhoneGap, Appery.io o algún otro.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    competencia_disenar_administrar_bases_datos = forms.ChoiceField(
        label='Establezca cual es su nivel de competencia para diseñar y administrar bases de datos con algunos gestores como SQL, MySQL, Oracle o alguna otra.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )

    competencia_disenar_gestionar_servicios_TI = forms.ChoiceField(
        label='Determine su nivel de competencia para diseñar y gestionar servicios de TI apegados a modelos y estándares como ITIL, COBIT, UML, CMMI, PMBOOK o algún otro.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )

    competencia_pruebas_software = forms.ChoiceField(
        label='Cuenta con la competencia para aplicar y utilizar técnicas y herramientas que lleven a cabo pruebas de software como Bugzilla, Testopia, FitNesse, qaManager, qaBook o alguna otra.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    
    
    seguridad_informacion_hacking = forms.ChoiceField(
        label='Considera usted que tiene los conocimientos necesarios para garantizar la seguridad en la información de los sistemas utilizando herramientas de seguridad y hacking de redes y sistemas de información.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    conocimientos_legales_tecnologias_informacion = forms.ChoiceField(
        label='Conoce usted los temas necesarios en el campo legal y jurídico en torno a las tecnologías de la información, el manejo de los derechos de autor y la privacidad de datos, así como conocimientos en Normas, estándares y prácticas de Seguridad de la Información.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    asesoria_sistemas_operativos = forms.ChoiceField(
        label='Determine su nivel de conocimiento para brindar asesoría en sistemas operativos como Linux, Mac, Windows, Solaris, entre otros.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    
    asesoria_arquitectura_computadoras = forms.ChoiceField(
        label='Cuenta con el conocimiento para brindar asesoría en arquitectura de computadoras como AMD, INTEL y MAC.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )

    conocimientos_analisis_diseno_pruebas = forms.ChoiceField(
        label='Tiene conocimientos para realizar Análisis y diseño de casos de pruebas, ejecución, levantamiento de defectos, Testing Funcional, Construcción y Ejecución de Entregables para la Metodología de pruebas aplicando Herramientas como QC, ALM, TFS ó Selenium entre otras.',
        choices=[(str(i), str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect
    )