import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { useNavigate } from "react-router-dom"; // ✅ Fixed import
import { postData } from "../services/api";

const OrganizationForm = () => {
    const navigate = useNavigate(); // ✅ Fixed navigation for React Router v6

    const formik = useFormik({
        initialValues: { name: "", contact_name: "", contact_phone: "", contact_email: "" },
        validationSchema: Yup.object({
            name: Yup.string().required("Name is required"),
            contact_name: Yup.string().required("Contact Name is required"),
            contact_phone: Yup.string().required("Phone is required"),
            contact_email: Yup.string().email("Invalid email").required("Email is required"),
        }),
        onSubmit: async (values) => {
            await postData("organizers", values);
            navigate("/organizations"); // ✅ Fixed navigation issue
        },
    });

    return (
        <form onSubmit={formik.handleSubmit}>
            <input name="name" placeholder="Organization Name" onChange={formik.handleChange} />
            <input name="contact_name" placeholder="Contact Name" onChange={formik.handleChange} />
            <input name="contact_phone" placeholder="Phone" onChange={formik.handleChange} />
            <input name="contact_email" placeholder="Email" onChange={formik.handleChange} />
            <button type="submit">Create</button>
        </form>
    );
};

export default CreateOrganization;
