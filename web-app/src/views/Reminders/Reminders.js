import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/styles';
import axios from 'axios';
import 
{
    Card,
    CardContent,
    Typography
} from '@material-ui/core';
import NotificationsActiveIcon from '@material-ui/icons/NotificationsActive';



const styles = theme => ({
    root: {
      background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
      border: 0,
      borderRadius: 3,
      boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
      color: 'white',
      height: 48,
      padding: '0 30px',
    },
    card: {
        borderRadius: 10,
        backgroundColor: theme.palette.warning.light,
        width: '40%',
        margin: '2%',

    },
    text:{
        color: theme.palette.black,
    }
  });


class Reminders extends Component{
    constructor(props){
        super(props);
        this.state = {
            reminderCards:[]
        };
    }
    componentDidMount(){
        var x = this;
        var reminderCards =[];
        var sse = new EventSource("http://localhost:5000/api/patient/get_remainders/"+localStorage.getItem("patient_id"));
        sse.onmessage = function(event){
            console.log(event.data);
            reminderCards.push(event.data);
            x.setState({reminderCards : reminderCards});
        }
        
        
    }
    
    render(){
        const { classes } = this.props;
        return(
        <div>
            {this.state.reminderCards.map(card => (
                   <Card className= {classes.card}>
                        <CardContent >
                            <NotificationsActiveIcon />
                            <Typography className={classes.text} variant='h4'>
                                
                                Reminder for getting Vaccination on {card}
                            </Typography>
                        </CardContent>
                    </Card>         
            ))}
            {/* *<Card className= {classes.card}>
                <CardContent >
                    <NotificationsActiveIcon />
                    <Typography className={classes.text} variant='h4'>
                        
                        Reminder for getting Vaccination on Date
                    </Typography>
                </CardContent>
            </Card>*/}
            </div>
        )
    }
}
Reminders.propTypes = {
    classes: PropTypes.object.isRequired,
  };


export default withStyles(styles)(Reminders);