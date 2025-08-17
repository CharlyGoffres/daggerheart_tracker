import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Item {
    id: rollsScreen
    
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
        anchors.margins: 20
        
        Column {
            width: parent.width
            spacing: 20
            
            // Header
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "🎲 TIRADAS DE DADOS"
                font.pixelSize: 36
                font.bold: true
                color: "#ffffff"
                
                DropShadow {
                    anchors.fill: parent
                    source: parent
                    radius: 8
                    samples: 16
                    color: Qt.rgba(0, 0, 0, 0.5)
                }
            }
            
            // Configuration Card
            Rectangle {
                width: parent.width
                height: configColumn.height + 40
                radius: 20
                color: Qt.rgba(52/255, 73/255, 94/255, 0.9) // #34495e with alpha
                
                Column {
                    id: configColumn
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "Configuración de Tirada"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    // Roll type selection
                    RowLayout {
                        width: parent.width
                        
                        Text {
                            text: "Tipo:"
                            font.pixelSize: 18
                            color: "#bdc3c7"
                            Layout.preferredWidth: 100
                        }
                        
                        ComboBox {
                            id: rollTypeCombo
                            Layout.fillWidth: true
                            model: ["Normal", "Ventaja", "Desventaja", "Doble Ventaja", "Triple Ventaja"]
                            currentIndex: 0
                            
                            background: Rectangle {
                                radius: 8
                                color: "#3498db"
                            }
                            
                            contentItem: Text {
                                text: rollTypeCombo.displayText
                                color: "#ffffff"
                                font.pixelSize: 16
                                verticalAlignment: Text.AlignVCenter
                                leftPadding: 10
                            }
                        }
                    }
                    
                    // Modifier selection
                    RowLayout {
                        width: parent.width
                        
                        Text {
                            text: "Modificador:"
                            font.pixelSize: 18
                            color: "#bdc3c7"
                            Layout.preferredWidth: 100
                        }
                        
                        ComboBox {
                            id: modifierCombo
                            Layout.fillWidth: true
                            model: ["Sin modificador", "+1", "+2", "1d4"]
                            currentIndex: 0
                            
                            background: Rectangle {
                                radius: 8
                                color: "#27ae60"
                            }
                            
                            contentItem: Text {
                                text: modifierCombo.displayText
                                color: "#ffffff"
                                font.pixelSize: 16
                                verticalAlignment: Text.AlignVCenter
                                leftPadding: 10
                            }
                        }
                    }
                }
            }
            
            // Results Display Card
            Rectangle {
                width: parent.width
                height: resultsColumn.height + 40
                radius: 20
                color: Qt.rgba(44/255, 62/255, 80/255, 0.9) // #2c3e50 with alpha
                
                Column {
                    id: resultsColumn
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "Resultado"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    // Dice display
                    Text {
                        id: diceDisplay
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "🎲 -- 🎲 --"
                        font.pixelSize: 48
                        color: "#f39c12"
                    }
                    
                    // Result text
                    Text {
                        id: resultText
                        anchors.horizontalCenter: parent.horizontalCenter
                        text: "Pulsa una habilidad para tirar dados"
                        font.pixelSize: 18
                        color: "#bdc3c7"
                        wrapMode: Text.Wrap
                        width: parent.width
                        horizontalAlignment: Text.AlignHCenter
                    }
                }
            }
            
            // Abilities Card
            Rectangle {
                width: parent.width
                height: abilitiesGrid.height + 80
                radius: 20
                color: Qt.rgba(52/255, 73/255, 94/255, 0.9)
                
                Column {
                    anchors.centerIn: parent
                    width: parent.width - 40
                    spacing: 15
                    
                    Text {
                        text: "Habilidades"
                        font.pixelSize: 24
                        font.bold: true
                        color: "#ecf0f1"
                    }
                    
                    GridLayout {
                        id: abilitiesGrid
                        width: parent.width
                        columns: 2
                        rowSpacing: 15
                        columnSpacing: 15
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Fuerza\n(+2)"
                            backgroundColor: "#e74c3c"
                            hoverColor: "#c0392b"
                            fontSize: 18
                            onClicked: rollAbility("Fuerza", 2)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Destreza\n(+1)"
                            backgroundColor: "#f39c12"
                            hoverColor: "#d68910"
                            fontSize: 18
                            onClicked: rollAbility("Destreza", 1)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Carisma\n(+0)"
                            backgroundColor: "#9b59b6"
                            hoverColor: "#8e44ad"
                            fontSize: 18
                            onClicked: rollAbility("Carisma", 0)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Constitución\n(+1)"
                            backgroundColor: "#27ae60"
                            hoverColor: "#229954"
                            fontSize: 18
                            onClicked: rollAbility("Constitución", 1)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Sabiduría\n(+0)"
                            backgroundColor: "#3498db"
                            hoverColor: "#2980b9"
                            fontSize: 18
                            onClicked: rollAbility("Sabiduría", 0)
                        }
                        
                        ModernButton {
                            Layout.fillWidth: true
                            Layout.preferredHeight: 80
                            text: "Inteligencia\n(-1)"
                            backgroundColor: "#95a5a6"
                            hoverColor: "#7f8c8d"
                            fontSize: 18
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
