import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

function Navbar() {
  const [menu,setmenu]=useState(false)
  const toggleMenu=()=>{
    setmenu(!menu)
  }

  return (
    <div className="">
      <div className="h-[2rem] w-full flex justify-between items-center p-8 text-[#FFFF] pt-10 relative z-50">
        <Link className="font-semibold">Timely</Link>
        {menu ? <div className="p-2 px-4 bg-white text-[#0e0e0e] rounded-lg md:hidden block cursor-pointer transition-all duration-75 ease-in" onClick={toggleMenu}>Close</div>:<div className="md:hidden block cursor-pointer transition-all duration-75 ease-out" onClick={toggleMenu}>Menu</div> }
        <div className="hidden text-[13px] md:flex gap-8 justify-between items-center font-regular">
          <Link className="py-2 px-6 rounded-lg border-[1px] border-[#FFF] cursor-pointer">
            template
          </Link>
          <Link className="py-2 px-6 rounded-lg bg-[#FFF] text-[#0E0E0E] cursor-pointer">
            schedule
          </Link>
        </div>
      </div>
      {menu && 
      <>
      <div className="md:hidden absolute bg-white h-auto w-full p-8 pb-10 z-50 transition-all duration-75 ease-in-out">
        <div className="grid gap-8">
          <Link className="text-[2rem] cursor-pointer">template</Link>
          <Link className="text-[2rem] cursor-pointer">schedule</Link>
        </div>
      </div>
      <div
            className="fixed inset-0 bg-black opacity-50 z-40"
            onClick={toggleMenu}
          ></div>
      </>
      }
    </div>
  );
}

export default Navbar;
