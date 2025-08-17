import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: rollsScreen
    
    // Optimización para pantallas 16:9
    property bool isWideScreen: width / height >= 1.6  // Para pantallas 16:9 o más anchas
    property bool isSmallScreen: width <= 800
    property real scaleFactor: isSmallScreen ? 0.8 : 1.0
    
    // Configuración específica para 16:9
    property int headerHeight: isWideScreen ? 100 : 120
    property int buttonHeight: isWideScreen ? 90 : 100
    property int cardPadding: isWideScreen ? 30 : 20
    
    // Beautiful gradient background specific to rolls
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { 
                position: 0.0
                color: Qt.rgba(255/255, 154/255, 158/255, 1.0) // #ff9a9e
            }
            GradientStop { 
                position: 1.0
                color: Qt.rgba(254/255, 207/255, 239/255, 1.0) // #fecfef
            }
        }
    }
    
    ScrollView {
        anchors.fill: parent
        anchors.margins: isWideScreen ? 30 : (isSmallScreen ? 10 : 20)
        
        Column {
            width: parent.width
            spacing: isWideScreen ? 25 : (isSmallScreen ? 15 : 20)
            
            // Header optimizado para 16:9 - más compacto horizontalmente
            Row {
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 40
                height: headerHeight
                
                // Dice visual horizontal para 16:9
                Row {
                    anchors.verticalCenter: parent.verticalCenter
                    spacing: 15
                    
                    Text {
                        text: "⚀"
                        font.pixelSize: isWideScreen ? 40 : (isSmallScreen ? 32 : 48)
                        color: "#ffffff"
                        rotation: -15
                    }
                    Text {
                        text: "⚁"
                        font.pixelSize: isWideScreen ? 40 : (isSmallScreen ? 32 : 48)
                        color: "#ffffff"
                        rotation: 15
                    }
                    Text {
                        text: "⚂"
                        font.pixelSize: isWideScreen ? 40 : (isSmallScreen ? 32 : 48)
                        color: "#ffffff"
                        rotation: -10
                    }
                    Text {
                        text: "⚃"
                        font.pixelSize: isWideScreen ? 40 : (isSmallScreen ? 32 : 48)
                        color: "#ffffff"
                        rotation: 20
                    }
                }
                
                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    text: "TIRADAS DE DADOS - DAGGERHEART"
                    font.pixelSize: isWideScreen ? 32 : (isSmallScreen ? 24 : 36)
                    font.bold: true
                    color: "#ffffff"
                }
            }
            
            // Layout optimizado para 16:9 - tres secciones horizontales
            Row {
                width: parent.width
                spacing: isWideScreen ? 40 : 30
                height: isWideScreen ? 180 : 200
                
                // Configuration Card - optimizada para 16:9
                Rectangle {
                    width: parent.width * (isWideScreen ? 0.35 : 0.5)
                    height: parent.height
                    radius: isWideScreen ? 15 : 20
                    color: Qt.rgba(52/255, 73/255, 94/255, 0.9)
                    
                    Column {
                        id: configColumn
                        anchors.centerIn: parent
                        width: parent.width - cardPadding
                        spacing: isWideScreen ? 12 : 15
                        
                        Text {
                            text: "Configuración"
                            font.pixelSize: isWideScreen ? 20 : 24
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        // Roll type y modifier optimizados para 16:9
                        Column {
                            width: parent.width
                            spacing: isWideScreen ? 10 : 12
                            
                            Row {
                                width: parent.width
                                spacing: 10
                                
                                Text {
                                    text: "Tipo:"
                                    font.pixelSize: isWideScreen ? 14 : 16
                                    color: "#bdc3c7"
                                    width: parent.width * 0.25
                                    anchors.verticalCenter: parent.verticalCenter
                                }
                                
                                ComboBox {
                                    id: rollTypeCombo
                                    width: parent.width * 0.7
                                    height: isWideScreen ? 35 : 40
                                    model: ["Normal", "Ventaja", "Desventaja", "Doble Ventaja", "Triple Ventaja"]
                                    currentIndex: 0
                                    
                                    background: Rectangle {
                                        radius: 6
                                        color: "#3498db"
                                    }
                                    
                                    contentItem: Text {
                                        text: rollTypeCombo.displayText
                                        color: "#ffffff"
                                        font.pixelSize: isWideScreen ? 13 : 16
                                        verticalAlignment: Text.AlignVCenter
                                        leftPadding: 8
                                    }
                                }
                            }
                            
                            Row {
                                width: parent.width
                                spacing: 10
                                
                                Text {
                                    text: "Modificador:"
                                    font.pixelSize: isWideScreen ? 14 : 16
                                    color: "#bdc3c7"
                                    width: parent.width * 0.25
                                    anchors.verticalCenter: parent.verticalCenter
                                }
                                
                                ComboBox {
                                    id: modifierCombo
                                    width: parent.width * 0.7
                                    height: isWideScreen ? 35 : 40
                                    model: ["Sin modificador", "+1", "+2", "1d4"]
                                    currentIndex: 0
                                    
                                    background: Rectangle {
                                        radius: 6
                                        color: "#27ae60"
                                    }
                                    
                                    contentItem: Text {
                                        text: modifierCombo.displayText
                                        color: "#ffffff"
                                        font.pixelSize: isWideScreen ? 13 : 16
                                        verticalAlignment: Text.AlignVCenter
                                        leftPadding: 8
                                    }
                                }
                            }
                        }
                    }
                }
                
                // Results Display Card - optimizada para 16:9
                Rectangle {
                    width: parent.width * (isWideScreen ? 0.35 : 0.45)
                    height: parent.height
                    radius: isWideScreen ? 15 : 20
                    color: Qt.rgba(44/255, 62/255, 80/255, 0.9)
                    
                    Column {
                        id: resultsColumn
                        anchors.centerIn: parent
                        width: parent.width - cardPadding
                        spacing: isWideScreen ? 8 : 15
                        
                        Text {
                            text: "Resultado"
                            font.pixelSize: isWideScreen ? 20 : 24
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        // Dice display optimizado
                        Text {
                            id: diceDisplay
                            anchors.horizontalCenter: parent.horizontalCenter
                            text: "🎲 -- 🎲 --"
                            font.pixelSize: isWideScreen ? 36 : 48
                            color: "#f39c12"
                        }
                        
                        // Result text compacto para 16:9
                        Text {
                            id: resultText
                            anchors.horizontalCenter: parent.horizontalCenter
                            text: "Pulsa una habilidad para tirar dados"
                            font.pixelSize: isWideScreen ? 14 : 18
                            color: "#bdc3c7"
                            wrapMode: Text.Wrap
                            width: parent.width
                            horizontalAlignment: Text.AlignHCenter
                        }
                    }
                }
                
                // Quick Stats Card - nueva sección para 16:9
                Rectangle {
                    width: parent.width * (isWideScreen ? 0.25 : 0.0)
                    height: parent.height
                    radius: isWideScreen ? 15 : 20
                    color: Qt.rgba(142/255, 68/255, 173/255, 0.9) // Purple accent
                    visible: isWideScreen
                    
                    Column {
                        anchors.centerIn: parent
                        width: parent.width - 20
                        spacing: 8
                        
                        Text {
                            text: "Stats Rápidas"
                            font.pixelSize: 16
                            font.bold: true
                            color: "#ecf0f1"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        Text {
                            text: "Éxito Crítico: 22+"
                            font.pixelSize: 12
                            color: "#f1c40f"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        Text {
                            text: "Éxito Mayor: 16-21"
                            font.pixelSize: 12
                            color: "#2ecc71"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        Text {
                            text: "Éxito Menor: 10-15"
                            font.pixelSize: 12
                            color: "#3498db"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                        
                        Text {
                            text: "Fallo: <10"
                            font.pixelSize: 12
                            color: "#e74c3c"
                            anchors.horizontalCenter: parent.horizontalCenter
                        }
                    }
                }
            }
            
            // Abilities Card - optimizada para 16:9
            Rectangle {
                width: parent.width
                height: isWideScreen ? (buttonHeight + 80) : (abilitiesGrid.height + 60)
                radius: isWideScreen ? 15 : 20
                color: Qt.rgba(52/255, 73/255, 94/255, 0.9)
                
                Column {
                    anchors.centerIn: parent
                    width: parent.width - (cardPadding * 2)
                    spacing: isWideScreen ? 15 : 20
                    
                    Text {
                        text: "Habilidades de Personaje"
                        font.pixelSize: isWideScreen ? 24 : 28
                        font.bold: true
                        color: "#ecf0f1"
                        anchors.horizontalCenter: parent.horizontalCenter
                    }
                    
                    // Grid optimizado para 16:9 - una sola fila si es posible
                    GridLayout {
                        id: abilitiesGrid
                        width: parent.width
                        columns: isWideScreen ? 6 : (isSmallScreen ? 3 : 6)
                        rows: isWideScreen ? 1 : 2
                        rowSpacing: isWideScreen ? 0 : 20
                        columnSpacing: isWideScreen ? 15 : 20
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Fuerza\n(+2)"
                            backgroundColor: "#e74c3c"
                            hoverColor: "#c0392b"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Fuerza", 2)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Destreza\n(+1)"
                            backgroundColor: "#f39c12"
                            hoverColor: "#d68910"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Destreza", 1)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Carisma\n(+0)"
                            backgroundColor: "#9b59b6"
                            hoverColor: "#8e44ad"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Carisma", 0)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Constitución\n(+1)"
                            backgroundColor: "#27ae60"
                            hoverColor: "#229954"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Constitución", 1)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Sabiduría\n(+0)"
                            backgroundColor: "#3498db"
                            hoverColor: "#2980b9"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Sabiduría", 0)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: buttonHeight
                            text: "Inteligencia\n(-1)"
                            backgroundColor: "#95a5a6"
                            hoverColor: "#7f8c8d"
                            fontSize: isWideScreen ? 16 : 20
                            onClicked: rollAbility("Inteligencia", -1)
                        }
                    }
                }
            }
        }
    }
    
    function rollAbility(abilityName, modifier) {
        var rollType = rollTypeCombo.currentText
        var modifierText = modifierCombo.currentText
        
        // Convert modifier text to number
        var extraModifier = 0
        if (modifierText === "+1") extraModifier = 1
        else if (modifierText === "+2") extraModifier = 2
        else if (modifierText === "1d4") extraModifier = Math.floor(Math.random() * 4) + 1
        
        // Start dice animation
        animateDiceRoll(abilityName, modifier, extraModifier, rollType)
    }
    
    function animateDiceRoll(ability, mod, extra, rollType) {
        // Animate rolling
        var animationFrames = 15
        var currentFrame = 0
        
        var rollTimer = Qt.createQmlObject('import QtQuick 2.15; Timer {}', rollsScreen)
        rollTimer.interval = 80
        rollTimer.repeat = true
        
        rollTimer.triggered.connect(function() {
            if (currentFrame < animationFrames) {
                var d1 = Math.floor(Math.random() * 12) + 1
                var d2 = Math.floor(Math.random() * 12) + 1
                diceDisplay.text = "🎲 " + d1 + " 🎲 " + d2
                currentFrame++
            } else {
                rollTimer.stop()
                rollTimer.destroy()
                
                // Calculate final result
                var dice = calculateDiceRoll(rollType)
                var total = dice[0] + dice[1] + mod + extra
                
                diceDisplay.text = "🎲 " + dice[0] + " 🎲 " + dice[1]
                
                var resultType = getResultType(total)
                var extraText = extra > 0 ? " + " + extra : ""
                var modText = mod !== 0 ? (mod > 0 ? " + " + mod : " " + mod) : ""
                
                resultText.text = ability + ": " + dice[0] + " + " + dice[1] + modText + extraText + " = " + total + "\n" + resultType
            }
        })
        
        rollTimer.start()
    }
    
    function calculateDiceRoll(rollType) {
        switch(rollType) {
            case "Normal":
                return [Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1]
            case "Ventaja":
                var rolls = [Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1]
                rolls.sort(function(a, b) { return b - a })
                return [rolls[0], rolls[1]]
            case "Desventaja":
                var rolls = [Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1]
                rolls.sort(function(a, b) { return a - b })
                return [rolls[0], rolls[1]]
            case "Doble Ventaja":
                var rolls = []
                for (var i = 0; i < 4; i++) rolls.push(Math.floor(Math.random() * 12) + 1)
                rolls.sort(function(a, b) { return b - a })
                return [rolls[0], rolls[1]]
            case "Triple Ventaja":
                var rolls = []
                for (var i = 0; i < 5; i++) rolls.push(Math.floor(Math.random() * 12) + 1)
                rolls.sort(function(a, b) { return b - a })
                return [rolls[0], rolls[1]]
            default:
                return [Math.floor(Math.random() * 12) + 1, Math.floor(Math.random() * 12) + 1]
        }
    }
    
    function getResultType(total) {
        if (total >= 22) return "🌟 ÉXITO CRÍTICO! 🌟"
        else if (total >= 16) return "⭐ Éxito Mayor ⭐"
        else if (total >= 10) return "✨ Éxito Menor ✨"
        else return "💥 Fallo 💥"
    }
}
