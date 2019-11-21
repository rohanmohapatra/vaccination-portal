import React, { useState, useEffect } from 'react';
import { Link as RouterLink, withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import validate from 'validate.js';
import { makeStyles } from '@material-ui/styles';
import axios from 'axios';
import clsx from 'clsx';
import {
  Grid,
  Button,
  IconButton,
  TextField,
  Link,
  FormHelperText,
  Checkbox,
  Typography
} from '@material-ui/core';

import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import ErrorIcon from '@material-ui/icons/Error';
import InfoIcon from '@material-ui/icons/Info';
import CloseIcon from '@material-ui/icons/Close';
import { amber, green } from '@material-ui/core/colors';
import Snackbar from '@material-ui/core/Snackbar';
import SnackbarContent from '@material-ui/core/SnackbarContent';
import WarningIcon from '@material-ui/icons/Warning';

const variantIcon = {
  success: CheckCircleIcon,
  warning: WarningIcon,
  error: ErrorIcon,
  info: InfoIcon,
};

const useStyles1 = makeStyles(theme => ({
  success: {
    backgroundColor: green[600],
  },
  error: {
    backgroundColor: theme.palette.error.dark,
  },
  info: {
    backgroundColor: theme.palette.primary.main,
  },
  warning: {
    backgroundColor: amber[700],
  },
  icon: {
    fontSize: 20,
  },
  iconVariant: {
    opacity: 0.9,
    marginRight: theme.spacing(1),
  },
  message: {
    display: 'flex',
    alignItems: 'center',
  },
}));

function MySnackbarContentWrapper(props) {
  const classes = useStyles1();
  const { className, message, onClose, variant, ...other } = props;
  const Icon = variantIcon[variant];

  return (
    <SnackbarContent
      className={clsx(classes[variant], className)}
      aria-describedby="client-snackbar"
      message={
        <span id="client-snackbar" className={classes.message}>
          <Icon className={clsx(classes.icon, classes.iconVariant)} />
          {message}
        </span>
      }
      action={[
        <IconButton key="close" aria-label="close" color="inherit" onClick={onClose}>
          <CloseIcon className={classes.icon} />
        </IconButton>,
      ]}
      {...other}
    />
  );
}

MySnackbarContentWrapper.propTypes = {
  className: PropTypes.string,
  message: PropTypes.string,
  onClose: PropTypes.func,
  variant: PropTypes.oneOf(['error', 'info', 'success', 'warning']).isRequired,
};

const useStyles2 = makeStyles(theme => ({
  margin: {
    margin: theme.spacing(1),
  },
}));


const schema = {
  firstName: {
    presence: { allowEmpty: false, message: 'is required' },
    length: {
      maximum: 32
    }
  },
  lastName: {
    presence: { allowEmpty: false, message: 'is required' },
    length: {
      maximum: 32
    }
  },
  email: {
    presence: { allowEmpty: false, message: 'is required' },
    email: true,
    length: {
      maximum: 64
    }
  },
  password: {
    presence: { allowEmpty: false, message: 'is required' },
    length: {
      maximum: 128
    }
  },
  policy: {
    presence: { allowEmpty: false, message: 'is required' },
    checked: true
  }
};

const useStyles = makeStyles(theme => ({
  root: {
    backgroundColor: theme.palette.background.default,
    height: '100%'
  },
  grid: {
    height: '100%'
  },
  quoteContainer: {
    [theme.breakpoints.down('md')]: {
      display: 'none'
    }
  },
  quote: {
    backgroundColor: theme.palette.neutral,
    height: '100%',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundImage: 'url(/images/auth.jpg)',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center'
  },
  quoteInner: {
    textAlign: 'center',
    flexBasis: '600px'
  },
  quoteText: {
    color: theme.palette.white,
    fontWeight: 300
  },
  name: {
    marginTop: theme.spacing(3),
    color: theme.palette.white
  },
  bio: {
    color: theme.palette.white
  },
  contentContainer: {},
  content: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column'
  },
  contentHeader: {
    display: 'flex',
    alignItems: 'center',
    paddingTop: theme.spacing(5),
    paddingBototm: theme.spacing(2),
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2)
  },
  logoImage: {
    marginLeft: theme.spacing(4)
  },
  contentBody: {
    flexGrow: 1,
    display: 'flex',
    alignItems: 'center',
    [theme.breakpoints.down('md')]: {
      justifyContent: 'center'
    }
  },
  form: {
    paddingLeft: 100,
    paddingRight: 100,
    paddingBottom: 125,
    flexBasis: 700,
    [theme.breakpoints.down('sm')]: {
      paddingLeft: theme.spacing(2),
      paddingRight: theme.spacing(2)
    }
  },
  title: {
    marginTop: theme.spacing(3)
  },
  textField: {
    marginTop: theme.spacing(2)
  },
  policy: {
    marginTop: theme.spacing(1),
    display: 'flex',
    alignItems: 'center'
  },
  policyCheckbox: {
    marginLeft: '-14px'
  },
  OrganizationButton: {
    margin: theme.spacing(2, 0)
  }
}));

const Organization = props => {
  const { history } = props;

  const classes = useStyles();

  const [formState, setFormState] = useState({
    isValid: true,
    values: {},
    touched: {},
    errors: {}
  });
  const [org, setOrg] = useState({});

  useEffect(() => {
    const errors = validate(formState.values, schema);

    setFormState(formState => ({
      ...formState,
      isValid: errors ? false : true,
      errors: errors || {}
    }));
    /*
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
    };
    fetchData();
    */

  }, [formState.values]);

  const handleChange = event => {
    event.persist();

    setFormState(formState => ({
      ...formState,
      values: {
        ...formState.values,
        [event.target.name]:
          event.target.type === 'checkbox'
            ? event.target.checked
            : event.target.value
      },
      touched: {
        ...formState.touched,
        [event.target.name]: true
      }
    }));
  };
  const [open, setOpen] = React.useState(false);
  const [eOpen, setEOpen] = React.useState(false);
  const handleClick = () => {
    setOpen(true);
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
    setEOpen(false);
  };


  const handleBack = () => {
    history.goBack();
  };

  const handleOrganization = event => {
    event.preventDefault();
    //history.push('/');
    console.log(formState.values);
    var date=formState.values.dateGiven.split('-');
    var data = {
      "patient_id": formState.values.patientId,
      "vaccination_id": formState.values.vaccinationId,
      "date_given" : date[2]+"/"+date[1]+"/"+date[0]
    }	
    console.log(date[2]+"/"+date[1]+"/"+date[0]);
    axios.post("http://localhost:5000/api/organization/add_patient_vaccination_data", data)
    .then(function(response){
      console.log(response);
      history.push("/organization/details");
      setOpen(true);
    })
    .catch(function(response){
      setEOpen(true);
    })
  };

  const hasError = field =>
    formState.touched[field] && formState.errors[field] ? true : false;

  return (
    <div className={classes.root}>
      <Grid
        className={classes.grid}
        container
      >
        <Grid
          className={classes.content}
          item
          lg={7}
          xs={12}
        >
          <div className={classes.content}>

            <div className={classes.contentBody}>
              <form
                className={classes.form}
                onSubmit={handleOrganization}
              >
                <Typography
                  className={classes.title}
                  variant="h2"
                >
                  Add A New Vaccination Record
                </Typography>
                <TextField
                  className={classes.textField}
                  error={hasError('patientId')}
                  fullWidth
                  helperText={
                    hasError('patientId') ? formState.errors.patientId[0] : null
                  }
                  label="Patient ID"
                  name="patientId"
                  onChange={handleChange}
                  type="text"
                  value={formState.values.patientId || ''}
                  variant="outlined"
                />
                <TextField
                  className={classes.textField}
                  error={hasError('vaccinationId')}
                  fullWidth
                  helperText={
                    hasError('vaccinationId') ? formState.errors.vaccinationId[0] : null
                  }
                  label="Vaccination ID"
                  name="vaccinationId"
                  onChange={handleChange}
                  type="text"
                  value={formState.values.vaccinationId || ''}
                  variant="outlined"
                />
                <TextField
                  id="date"
                  label="Date"
                  type="date"
                  name="dateGiven"
                  onChange={handleChange}
                  defaultValue=""
                  className={classes.textField}
                  InputLabelProps={{
                    shrink: true,
                  }}
                />
               
                <Button
                  className={classes.OrganizationButton}
                  color="primary"
                  disabled={formState.isValid}
                  fullWidth
                  size="large"
                  type="submit"
                  variant="contained"
                >
                  Add Record
                </Button>
              </form>
              <Snackbar
                anchorOrigin={{vertical: 'bottom',horizontal: 'right'}}
                open={open}
                autoHideDuration={6000}
                onClose={handleClose}
              >
                <MySnackbarContentWrapper
                  onClose={handleClose}
                  variant="success"
                  message="Successfully Added!"
                />
              </Snackbar>
              <Snackbar
                anchorOrigin={{vertical: 'bottom',horizontal: 'right'}}
                open={eOpen}
                autoHideDuration={6000}
                onClose={handleClose}
              >
                <MySnackbarContentWrapper
                  onClose={handleClose}
                  variant="error"
                  message="Error Adding Record"
                />
              </Snackbar>
            </div>
          </div>
        </Grid>
      </Grid>
    </div>
  );
};

Organization.propTypes = {
  history: PropTypes.object
};

export default withRouter(Organization);