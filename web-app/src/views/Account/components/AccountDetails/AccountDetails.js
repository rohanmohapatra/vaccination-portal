import React, { useState , useEffect} from 'react';
import clsx from 'clsx';
import axios from 'axios';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import {
  Card,
  CardHeader,
  CardContent,
  CardActions,
  Divider,
  Grid,
  Button,
  TextField,
  Typography
} from '@material-ui/core';

const useStyles = makeStyles(() => ({
  root: {}
}));

const AccountDetails = props => {
  const { className, ...rest } = props;
  
  const classes = useStyles();

  const [values, setValues] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        'http://localhost:5000/api/patient/get_personal_details/p0001',
      );
      setValues(result.data["organization"]);
      console.log(result.data);
    };
    fetchData();
    console.log(values);
  }, []);
  const handleChange = event => {
    setValues({
      ...values,
      [event.target.name]: event.target.value
    });
  };

  const states = [
    {
      value: 'alabama',
      label: 'Alabama'
    },
    {
      value: 'new-york',
      label: 'New York'
    },
    {
      value: 'san-francisco',
      label: 'San Francisco'
    }
  ];

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <form
        autoComplete="off"
        noValidate
      >
        <CardHeader
          subheader=""
          title="Organization Details"
        />
        <Divider />
        <CardContent>
          <Grid
            container
            spacing={3}
          >
            {values.map(option => (
                  <Grid
                  item
                  md={6}
                  xs={12}
                >
              <Typography variant="h1" component="h2">
                {option}
              </Typography>
                  
                </Grid>
              ))};
            
          </Grid>
        </CardContent>
        <Divider />
      </form>
    </Card>
  );
};

AccountDetails.propTypes = {
  className: PropTypes.string
};

export default AccountDetails;
