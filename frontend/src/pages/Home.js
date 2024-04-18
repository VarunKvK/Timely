import React from "react";
import Navbar from "../components/navbar";
import { Link } from "react-router-dom";
function Home() {
  return (
    <div className="h-[88vh] w-full pl-4 pr-4">
      <div className="bgcolor h-[88vh] rounded-2xl flex items-center justify-center">
        <div className="">
          <div className="flex items-center justify-center">
            <h1 className="text-[80px] font-medium text-center w-[60%] text-white leading-[4.5rem]">
              You <span className="font-extralight italic">schedule</span> we
              <span className="font-extralight italic"> manage</span> them
            </h1>
          </div>
          <div className="flex items-center justify-center mt-4">
            <p className="text-center text-white w-[70%] font-regular">
              Timely allows users to send emails to a large number of people
              with ease. all you need to give is the list of leads you want to
              send and select the template you want or create a custom template.
            </p>
          </div>
          <div className="flex justify-evenly items-center">
            <div className="flex gap-4 pt-4">
              <Link className="py-2 px-6 font-medium text-[15px] rounded-lg bg-[#FFF] text-[#0E0E0E] cursor-pointer flex items-center">
                Schedule Emails
              </Link>
              <Link className="py-2 px-6 rounded-lg font-medium text-[15px] border-[1px] border-[#FFF] text-white cursor-pointer flex items-center">
                Create Templates
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
