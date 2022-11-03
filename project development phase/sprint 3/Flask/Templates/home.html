import React from 'react'
import { StyleSheet, Button, Text, View, Linking } from 'react-native'
import firebase from 'react-native-firebase'
const auth = firebase.auth();
const firestore = firebase.firestore();
const users = firestore.collection("users");


export default class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: auth.currentUser.email,
      lat: null,
      long: null,
      locations: []
    }
    this.enableEmergency = this.enableEmergency.bind(this)
    this.disableEmergency = this.disableEmergency.bind(this)
    this.componentDidMount = this.componentDidMount.bind(this)
  }

  componentDidMount() {
    var self = this;
    users.where("email", "==", auth.currentUser.email).get().then(function (querySnapshot) {
      var user_data = querySnapshot.docs[0].data()
      self.setState({
        name: user_data.name,
        role: user_data.role
      })
      if(user_data.role == "user"){
        self.setState({
          emergency: user_data.emergency
        });
        if (user_data.emergency){
          console.log("Emergency Enabled! ")
        }
      }
      else{
        users.where("emergency","==", true).onSnapshot(function(querySnapshot){
          var docs = querySnapshot.docs
          var locations = [];
          docs.forEach((doc)=>{
            locations.push(doc.data().location)
          })
          self.setState({
            emergency_count: docs.length
          })
          console.log("Emergency count is "+docs.length)
          console.log("Locations of emergency are - ")
          console.log(locations)
        })
      }
    }).catch((err) => {
      console.log("Error: Document not found ", err);
    })
  }

  handleLogout() {
    auth.signOut().then(function () {
      this.props.navigation.navigate('LoginScreen');
    }).catch(function (err) {
      console.log(err);
    })
  }

  enableEmergency() {
    var self = this;
    var lat = 0; var long = 0;
    users.where("email", "==", this.state.email).get().then(function (querySnapshot) {
      var id = querySnapshot.docs[0].id;
      console.log(id + ' clicked Emergency');
      navigator.geolocation.getCurrentPosition(function (position) {
        lat = position.coords.latitude;
        long = position.coords.longitude;
        self.setState({
          lat, long
        });
        users.doc(id).set({
          emergency: true,
          location: new firebase.firestore.GeoPoint(lat, long)
        }, { merge: true }).then(() => {
          console.log("Emergency activated");
          self.setState({
            emergency: true
          })
        }).catch((err) => {
          console.log("Error writing document: ", err);
        })
        console.log(position.coords.latitude, self.state.long);
      }, function (err) {
        console.log("Error: " + err);
        throw err;
      }, { enableHighAccuracy: false, timeout: 20000 });
    }).catch((err) => {
      console.log("Error: Document not found ", err);
    })
  }

  disableEmergency() {
    var self = this;
    users.where("email", "==", this.state.email).get().then(function (querySnapshot) {
      var id = querySnapshot.docs[0].id
      console.log(id + ' disabled Emergency')
      users.doc(id).set({
        emergency: false
      }, { merge: true }).then(() => {
        console.log("Emergency disabled");
        self.setState({
          emergency: false
        })
      }).catch((err) => {
        console.log("Error writing document: ", error);
      })
    }).catch((err) => {
      console.log("Error: Document not found ", error);
    })
  }

  handleDial() {
    call_url = "tel:9004245501"
    Linking.openURL(call_url).catch(err => console.error('An error occurred', err));
  }

  render() {
    const enable_emergency = (
      <Button
        title="Enable Emergency"
        onPress={this.enableEmergency}
      />
    )

    const disable_emergency = (
      <Button
        title="Disable Emergency"
        onPress={this.disableEmergency}
      />
    )
    
    const user_content = (
      <View style={styles.container}>
        <Text style={styles.heading}>
        {this.state.name ? "Hi " + this.state.name + "!" : null}
        </Text>
        {this.state.emergency ? disable_emergency : enable_emergency}
        <Button
          title="Call Helpline"
          onPress={this.handleDial}
        />
        <Button
          title="Logout"
          onPress={this.handleLogout}
        />
      </View>
    )

    const printLocations = (
      <View>
      {
        this.state.locations.map((location) => {
        <Text>{location._latitude} {location._longitude}</Text>  
        })
      }
      </View>
    )

    const admin_content = (
      <View style={styles.container}>
        <Text style={styles.heading}>{this.state.name ? "Hi " + this.state.name + "!" : null}</Text>
        <Text style={styles.heading}>{this.state.emergency_count? "There are currently": null}</Text>
        <Text style={styles.heading}>{this.state.emergency_count}</Text>
        <Text style={styles.heading}>{this.state.emergency_count? "Emergencies": null}</Text>
        {printLocations} 
        <Button
          title="Logout"
          onPress={this.handleLogout}
        />
      </View>
    )

    return (
      <View style={styles.container}>
        {this.state.role == "user"? user_content: admin_content}
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  heading: {
    fontSize: 25,
  }
})