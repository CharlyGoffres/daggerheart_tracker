# 🎲 Daggerheart Tracker - Modern Edition

Una aplicación hermosa y moderna para gestionar personajes de Daggerheart RPG, completamente rediseñada con Qt/QML.

## ✨ Características Principales

### 🎨 Diseño Visual Radical
- **Interfaz moderna** con Qt Material Design
- **QML responsive** con componentes nativos
- **Animaciones fluidas** y transiciones suaves
- **Responsive design** que se adapta a diferentes tamaños de pantalla
- **Cross-platform** - funciona en Windows, macOS, Linux

### 🎲 Sistema de Tiradas Avanzado
- **Animaciones de dados** con Qt Quick
- **Múltiples tipos de tirada**: Normal, Ventaja, Desventaja, Doble/Triple Ventaja
- **Modificadores personalizables**: +1, +2, 1d4
- **Análisis automático** de éxito/fallo con umbrales configurables
- **Interfaz intuitiva** con resultados detallados

### ⚔️ Gestión Completa de Personajes
- **Ficha interactiva** con todas las estadísticas
- **Edición en tiempo real** de habilidades, HP, armadura
- **Sistema de umbrales** para diferentes niveles de dificultad
- **Guardado automático** de cambios
- **Interfaz touch-friendly** para tablets y pantallas táctiles

### ⚙️ Configuración Avanzada
- **Múltiples temas** y opciones de personalización
- **Control de animaciones** y efectos visuales
- **Exportación de datos** del personaje
- **Reset rápido** para comenzar nuevas aventuras

## 🚀 Cómo Ejecutar

### Requisitos
- Python 3.8 o superior
- PySide6 (Qt for Python)

### Instalación
```bash
# Clonar o descargar el proyecto
cd daggerheart_trackers

# Instalar dependencias Qt
pip install -r requirements_qt.txt

# Ejecutar la aplicación
python main_qt.py
```

## 📱 Pantallas Principales

### 🏠 Menú Principal
- **Gradiente épico** morado-azul de fondo
- **Tarjetas de navegación** con descripciones
- **Botones animados** con efectos hover
- **Tipografía llamativa** con iconos temáticos

### 🎲 Tiradas de Dados
- **Fondo oscuro elegante** para mejor contraste
- **Configuración visual** de tipos de tirada
- **Botones de habilidades** con colores únicos
- **Animación de dados** con cambios de color
- **Resultados detallados** con análisis de éxito

### ⚔️ Ficha de Personaje
- **Diseño por secciones** con tarjetas temáticas
- **Colores por categoría**: rojo para vida, verde para habilidades
- **Inputs interactivos** con validación en tiempo real
- **Guardado visual** con feedback inmediato

### ⚙️ Configuración
- **Controles modernos** (switches, sliders)
- **Organización por categorías** de ajustes
- **Acciones rápidas** para gestión de datos
- **Información de la app** con versión

## 🎨 Paleta de Colores

- **Primario**: Gradientes morado-azul (#667eea → #764ba2)
- **Secundario**: Verde esmeralda (#27ae60) para éxitos
- **Acento**: Dorado (#f1c40f) para elementos importantes  
- **Peligro**: Rojo (#e74c3c) para vida baja y fallos
- **Fondo**: Gris oscuro (#2c3e50) para contraste
- **Texto**: Blanco/gris claro para legibilidad

## 🔧 Arquitectura Técnica

### Estructura del Proyecto
```
daggerheart_trackers/
├── main.py                 # Aplicación principal
├── screens/               
│   ├── menu.py            # Menú principal moderno
│   ├── rolls.py           # Sistema de tiradas avanzado
│   ├── characteristics.py # Ficha de personaje interactiva
│   └── settings.py        # Configuración moderna
├── utils/
│   └── settings.py        # Gestor de configuración
└── README.md              # Este archivo
```

### Componentes Modernos
- **ModernButton**: Botones con animaciones hover
- **Card System**: Tarjetas con esquinas redondeadas
- **Gradient Backgrounds**: Fondos con gradientes suaves
- **Responsive Layout**: Diseño adaptativo

## 🎮 Características del Juego

### Sistema de Habilidades
- **6 Habilidades principales**: Fuerza, Destreza, Carisma, Constitución, Sabiduría, Inteligencia
- **Modificadores editables** de -3 a +5
- **Colores únicos** para cada habilidad

### Umbrales de Dificultad
- **Menor**: 10+ (Éxito básico)
- **Mayor**: 16+ (Éxito notable)  
- **Severo**: 22+ (Éxito crítico)

### Sistema de Vida
- **HP actual/máximo** editable
- **Indicadores visuales** de estado de salud
- **Armadura** configurable

## 📝 Changelog v2.0

### ✅ Cambios Radicales
- ❌ **Eliminación completa** del sistema GPIO
- 🎨 **Rediseño total** de la interfaz
- ✨ **Nuevas animaciones** y efectos visuales
- 📱 **Diseño responsive** mejorado
- 🎲 **Sistema de tiradas** más avanzado
- ⚔️ **Gestión de personajes** ampliada
- ⚙️ **Configuración** más completa

### 🔧 Mejoras Técnicas
- 🏗️ **Arquitectura modular** mejorada
- 🎯 **Kivy 2.0+** como framework base
- 💾 **Sistema de guardado** robusto
- 🔄 **Transiciones** suaves entre pantallas

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🎲 ¡Que disfrutes tus aventuras!

Creado con ❤️ para la comunidad de Daggerheart RPG.
