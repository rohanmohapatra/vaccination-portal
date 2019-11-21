import React, {useEffect, useState}from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import clsx from 'clsx';
import moment from 'moment';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardActions,
  CardContent,
  Avatar,
  Typography,
  Divider,
  Button,
  LinearProgress
} from '@material-ui/core';
import { amber, green, red } from '@material-ui/core/colors';

const useStyles = makeStyles(theme => ({
  root: {},
  details: {
    display: 'flex'
  },
  avatar: {
    height: 110,
    width: 100,
    flexShrink: 0,
    flexGrow: 0
  },
  progress: {
    marginTop: theme.spacing(2)
  },
  uploadButton: {
    marginRight: theme.spacing(2)
  }
}));

const AccountProfile = props => {
  const { className, ...rest } = props;

  const classes = useStyles();

  const user = {
    name: 'Shen Zhi',
    city: 'Los Angeles',
    country: 'USA',
    timezone: 'GTM-7',
    avatar: '/images/avatars/avatar_11.png'
  };
  const [profile, setProfile] = useState({});
  const [statusColor, getStatusColor] = useState("");
  const [status, setStatus] = useState("");
  useEffect(() => {
    const fetchData = async () => {
      const result2 = await axios({
        method: 'post',
        url:  'http://localhost:5000/api/patient/get_patient_id/',
        data: {"username" : localStorage.getItem("username")},
      });
      //setProfile(result.data);
      localStorage.setItem("patient_id",result2.data["patient_id"])
      //console.log(result.data);
      const result = await axios(
        'http://localhost:5000/api/patient/get_personal_details/'+localStorage.getItem("patient_id"),
      );
      setProfile(result.data);
      console.log(result.data);
      const result3 = await axios({
        method: 'post',
        url:  'http://localhost:5000/api/patient/predict_patient/',
        data: {"username" : localStorage.getItem("username")},
      });
      switch(result3.data["status"]){
        case "poor" : 
              getStatusColor(red[700]);
              setStatus("Incomplete");
              break;
        case "medium":
              getStatusColor(amber[700]);
              setStatus("Partial");
              break;
        case "complete":
              getStatusColor(green[600]);
              setStatus("Completed");
              break;
      }
    };
    fetchData();
    console.log(profile);
  }, []);
  var cardBacground = {
    backgroundColor: statusColor,
    marginBottom: 40,
    padding: 10,
    borderRadius : 50
  }
  return (
    <div>
    <Card style ={cardBacground}>
      <Typography variant="h3">Vaccination Status:  {status}</Typography>
    </Card>
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <CardContent>
        <div className={classes.details}>
          <div>
          <Avatar
            alt="Person"
            className={classes.avatar}
            src="https://github.com/identicons/jasonlong.png"
            to=""
          />
            <Divider />

            <Typography
              gutterBottom
              variant="h2"
            >
              {profile.patient_name}
            </Typography>
            <Typography
              className={classes.locationText}
              color="textSecondary"
              variant="body1"
            >
              {profile.city_of_birth}
            </Typography>
            <Typography
              className={classes.dateText}
              color="textSecondary"
              variant="body1"
            >
              Date of Birth : {profile.dob}
            </Typography>
            <Typography
              className={classes.locationText}
              color="textSecondary"
              variant="body1"
            >
              {profile.email_address}
            </Typography>
            <Typography
              className={classes.locationText}
              color="textSecondary"
              variant="h4"
            >
              Father's Name: {profile.father_name}
            </Typography>
            <Typography
              className={classes.locationText}
              color="textSecondary"
              variant="h4"
            >
              Mother's Name: {profile.mother_name}
            </Typography>
            <Typography
              className={classes.locationText}
              color="textSecondary"
              variant="h4"
            >
              {profile.phone_number}
            </Typography>
          </div>
          
        </div>
        
      </CardContent>
      <Divider />
    </Card>
    </div>
  );
};

AccountProfile.propTypes = {
  className: PropTypes.string
};

export default AccountProfile;
