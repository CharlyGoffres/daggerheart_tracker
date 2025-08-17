import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtGraphicalEffects 1.15

Rectangle {
    id: card
    width: parent.width
    height: 100
    radius: 20
    color: Qt.rgba(1, 1, 1, 0.95)
    
    property string title: ""
    property string subtitle: ""
    property color cardColor: "#3498db"
    
    signal clicked()
    
    // Card content
    RowLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 20
        
        // Icon section
        Rectangle {
            Layout.preferredWidth: 60
            Layout.preferredHeight: 60
            radius: 15
            color: card.cardColor
            
            // Icon would go here - for now just colored rectangle
        }
        
        // Content section
        Column {
            Layout.fillWidth: true
            spacing: 5
            
            Text {
                text: card.title
                font.pixelSize: 22
                font.bold: true
                color: "#2c3e50"
                wrapMode: Text.Wrap
                width: parent.width
            }
            
            Text {
                text: card.subtitle
                font.pixelSize: 16
                color: "#7f8c8d"
                wrapMode: Text.Wrap
                width: parent.width
            }
        }
    }
    
    // Click area
    MouseArea {
        anchors.fill: parent
        hoverEnabled: true
        
        onClicked: card.clicked()
        
        onEntered: {
            scaleAnimation.to = 1.02
            scaleAnimation.start()
        }
        
        onExited: {
            scaleAnimation.to = 1.0
            scaleAnimation.start()
        }
        
        onPressed: {
            scaleAnimation.to = 0.98
            scaleAnimation.start()
        }
        
        onReleased: {
            scaleAnimation.to = 1.02
            scaleAnimation.start()
        }
    }
    
    // Hover animation
    PropertyAnimation {
        id: scaleAnimation
        target: card
        property: "scale"
        duration: settings.animationsEnabled ? 150 : 0
        easing.type: Easing.OutQuad
    }
    
    // Drop shadow
    DropShadow {
        anchors.fill: card
        source: card
        radius: 8
        samples: 16
        color: Qt.rgba(0, 0, 0, 0.1)
        cached: true
    }
}
