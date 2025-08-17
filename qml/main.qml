import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15

ApplicationWindow {
    id: window
    visible: true
    width: 1200
    height: 800
    minimumWidth: 800
    minimumHeight: 600
    title: "Daggerheart Tracker"
    
    property bool isDarkTheme: settings.darkTheme
    
    // Color scheme
    property color primaryColor: "#667eea"
    property color secondaryColor: "#764ba2"
    property color backgroundLight: "#f8f9fa"
    property color backgroundDark: "#2c3e50"
    property color cardColor: isDarkTheme ? "#34495e" : "#ffffff"
    property color textColor: isDarkTheme ? "#ecf0f1" : "#2c3e50"
    property color accentColor: "#3498db"
    
    // Gradient background
    Rectangle {
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { 
                position: 0.0
                color: Qt.rgba(102/255, 126/255, 234/255, 1.0) // #667eea
            }
            GradientStop { 
                position: 1.0
                color: Qt.rgba(118/255, 75/255, 162/255, 1.0) // #764ba2
            }
        }
    }
    
    // Main content area
    StackView {
        id: stackView
        anchors.fill: parent
        anchors.bottomMargin: bottomNavigation.height
        
        initialItem: MenuScreen {}
        
        pushEnter: Transition {
            PropertyAnimation {
                property: "x"
                from: stackView.width
                to: 0
                duration: settings.animationsEnabled ? 300 : 0
                easing.type: Easing.OutCubic
            }
        }
        
        pushExit: Transition {
            PropertyAnimation {
                property: "x"
                from: 0
                to: -stackView.width
                duration: settings.animationsEnabled ? 300 : 0
                easing.type: Easing.OutCubic
            }
        }
    }
    
    // Bottom Navigation
    BottomNavigation {
        id: bottomNavigation
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        height: 80
        
        onScreenRequested: function(screenName) {
            switchToScreen(screenName)
        }
    }
    
    // Screen switching function
    function switchToScreen(screenName) {
        var component
        
        switch(screenName) {
            case "menu":
                component = Qt.createComponent("MenuScreen.qml")
                break
            case "rolls":
                component = Qt.createComponent("RollsScreen.qml")
                break
            case "character":
                component = Qt.createComponent("CharacterScreen.qml")
                break
            case "combat":
                component = Qt.createComponent("CombatScreen.qml")
                break
            case "settings":
                component = Qt.createComponent("SettingsScreen.qml")
                break
            default:
                console.log("Unknown screen:", screenName)
                return
        }
        
        if (component.status === Component.Ready) {
            stackView.push(component)
            app.switchScreen(screenName)
        } else {
            console.log("Error loading screen:", component.errorString())
        }
    }
    
    // Handle back button
    onClosing: function(close) {
        if (stackView.depth > 1) {
            close.accepted = false
            stackView.pop()
        } else {
            app.exitApp()
        }
    }
}
