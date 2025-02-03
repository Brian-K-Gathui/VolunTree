import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar"; 
import Footer from "./components/Footer"; 
import Home from "./pages/Home";
import Login from "./pages/adminPages/LoginAdmin";  
import SignUp from "./pages/adminPages/SignUpAdmin";  
import EditAdmin from "./pages/adminPages/EditAdmin";

import OrganizationList from "./pages/organizationPages/OrganizationList";  
import CreateOrganization from "./pages/organizationPages/CreateOrganization"; 
import EditOrganization from "./pages/organizationPages/EditOrganization"; 

import VolunteerList from "./pages/volunteerPages/VolunteerList";  
import CreateVolunteer from "./pages/volunteerPages/CreateVolunteer"; 
import EditVolunteer from "./pages/volunteerPages/EditVolunteer"; 

import EventList from "./pages/eventPages/EventList"; 
import CreateEvent from "./pages/eventPages/CreateEvent"; 
import EditEvent from "./pages/eventPages/EditEvent"; 

import TaskList from "./pages/taskPages/TaskList"; 
import CreateTask from "./pages/taskPages/CreateTask"; 
import EditTask from "./pages/taskPages/EditTask"; 

import NotFound from "./pages/notfound"; 

const App = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />
                <Route path="/admin/edit/:id" element={<EditAdmin />} />

                <Route path="/organizations" element={<OrganizationList />} />
                <Route path="/organizations/create" element={<CreateOrganization />} />
                <Route path="/organizations/edit/:id" element={<EditOrganization />} />

                <Route path="/volunteers" element={<VolunteerList />} />
                <Route path="/volunteers/create" element={<CreateVolunteer />} />
                <Route path="/volunteers/edit/:id" element={<EditVolunteer />} />

                <Route path="/events" element={<EventList />} />
                <Route path="/events/create" element={<CreateEvent />} />
                <Route path="/events/edit/:id" element={<EditEvent />} />

                <Route path="/tasks" element={<TaskList />} />
                <Route path="/tasks/create" element={<CreateTask />} />
                <Route path="/tasks/edit/:id" element={<EditTask />} />

                <Route path="*" element={<NotFound />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
