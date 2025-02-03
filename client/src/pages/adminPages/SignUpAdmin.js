import React from "react";
import { useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import * as Yup from "yup";
import { postData } from "../services/api";

const SignUp = () => {
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      first_name: "",
      last_name: "",
      email: "",
      username: "",
      password: "",
    },
    validationSchema: Yup.object({
      first_name: Yup.string().required("First name is required"),
      last_name: Yup.string().required("Last name is required"),
      email: Yup.string().email("Invalid email format").required("Email is required"),
      username: Yup.string().required("Username is required"),
      password: Yup.string()
        .min(6, "Password must be at least 6 characters")
        .required("Password is required"),
    }),
    onSubmit: async (values) => {
      const response = await postData("admin/signup", values);

      if (response.error) {
        alert(response.error);
      } else {
        alert("Sign-up successful!");
        navigate("/login"); // Redirect to login page after successful sign-up
      }
    },
  });

  return (
    <div className="dashboard-container">
      <h1>VolunTree Admin Sign Up 🌳</h1>
      <form onSubmit={formik.handleSubmit} className="login-form">
        <input
          type="text"
          name="first_name"
          placeholder="First Name"
          onChange={formik.handleChange}
          value={formik.values.first_name}
          className="form-control"
        />
        {formik.errors.first_name && formik.touched.first_name && (
          <div className="error">{formik.errors.first_name}</div>
        )}

        <input
          type="text"
          name="last_name"
          placeholder="Last Name"
          onChange={formik.handleChange}
          value={formik.values.last_name}
          className="form-control"
        />
        {formik.errors.last_name && formik.touched.last_name && (
          <div className="error">{formik.errors.last_name}</div>
        )}

        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={formik.handleChange}
          value={formik.values.email}
          className="form-control"
        />
        {formik.errors.email && formik.touched.email && (
          <div className="error">{formik.errors.email}</div>
        )}

        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={formik.handleChange}
          value={formik.values.username}
          className="form-control"
        />
        {formik.errors.username && formik.touched.username && (
          <div className="error">{formik.errors.username}</div>
        )}

        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={formik.handleChange}
          value={formik.values.password}
          className="form-control"
        />
        {formik.errors.password && formik.touched.password && (
          <div className="error">{formik.errors.password}</div>
        )}

        <button type="submit" className="btn-primary">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUp;
