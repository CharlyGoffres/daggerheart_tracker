import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Button {
    id: modernButton
    
    property color backgroundColor: "#3498db"
    property color hoverColor: "#2980b9"
    property color pressedColor: "#1f5f8b"
    property color textColor: "#ffffff"
    property int fontSize: 16
    property bool roundedCorners: true
    
    background: Rectangle {
        id: buttonBackground
        radius: modernButton.roundedCorners ? 15 : 0
        color: modernButton.pressed ? modernButton.pressedColor : 
               (modernButton.hovered ? modernButton.hoverColor : modernButton.backgroundColor)
        
        Behavior on color {
            ColorAnimation {
                duration: settings.animationsEnabled ? 150 : 0
                easing.type: Easing.OutQuad
            }
        }
        
        // Drop shadow
        DropShadow {
            anchors.fill: buttonBackground
            source: buttonBackground
            radius: 4
            samples: 8
            color: Qt.rgba(0, 0, 0, 0.3)
            cached: true
        }
    }
    
    contentItem: Text {
        text: modernButton.text
        font.pixelSize: modernButton.fontSize
        font.bold: true
        color: modernButton.textColor
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        wrapMode: Text.Wrap
    }
    
    // Scale animation
    scale: pressed ? 0.95 : (hovered ? 1.05 : 1.0)
    
    Behavior on scale {
        PropertyAnimation {
            duration: settings.animationsEnabled ? 100 : 0
            easing.type: Easing.OutQuad
        }
    }
}
