import React from "react";
import Navbar from "../components/navbar";
import { Link } from "react-router-dom";
function Home() {
  return (
    <div className="2xl:h-[92vh] xl:h-[88vh] lg:h-[88vh] md:h-[86vh] sm:h-[90vh] h-[86vh] w-full pl-4 pr-4">
      <div className="bgcolor 2xl:h-full xl:h-[88vh] lg:h-[88vh] md:h-[86vh] sm:h-[85vh] h-[86vh] rounded-2xl flex items-center justify-center">
        <div className="">
          <div className="flex items-center justify-center">
            <h1 className="text-[40px] 2xl:text-[90px] xl:text-[70px] lg:text-[65px] md:text-[55px] sm:text-[55px] font-medium text-center xl:w-[60%] lg:w-[80%] md:w-[75%] sm:w-[75%] w-full text-white 2xl:leading-[6rem] xl:leading-[5.5rem] lg:leading-[5rem] md:leading-[3.5rem] sm:leading-[4rem] leading-[2.4rem]">
              You <span className="font-extralight italic">schedule</span> we
              <span className="font-extralight italic"> manage</span> them
            </h1>
          </div>
          <div className="flex items-center justify-center 2xl:mt-[3rem] lg:mt-[1.5rem] md:mt-4 sm:mt-8 mt-[1rem]">
            <p className="text-center text-white 2xl:w-[45%] xl:w-[50%] lg:w-[60%] md:w-[55%] sm:w-[70%] w-[84%] 2xl:text-[1.3rem] xl:text-[1rem] lg:text-[0.9rem] md:text-[0.8rem] sm:text-[0.9rem] text-[0.7rem] font-regular">
              Timely allows users to send emails to a large number of people
              with ease. all you need to give is the list of leads you want to
              send and select the template you want or create a custom template.
            </p>
          </div>
          <div className="flex justify-evenly items-center">
            <div className="flex 2xl:gap-12 gap-4 pt-4 2xl:pt- xl:pt-8 lg:pt-[1.5rem]">
              <Link className="2xl:py-4 2xl:px-10 py-2 px-6 font-medium 2xl:text-[20px] xl:text-[17px] lg:text-[15px] md:text-[12px] sm:text-[12px] text-[12px] 2xl:rounded-2xl rounded-lg bg-[#FFF] text-[#0E0E0E] cursor-pointer flex items-center">
                Schedule Emails
              </Link>
              <Link className="2xl:py-4 2xl:px-10 py-2 px-6 2xl:rounded-2xl rounded-lg font-medium 2xl:text-[20px] xl:text-[17px] lg:text-[15px] md:text-[12px] sm:text-[12px] text-[12px] border-[1px] border-[#FFF] text-white cursor-pointer flex items-center">
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
