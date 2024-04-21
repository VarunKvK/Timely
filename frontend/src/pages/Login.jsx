import React from 'react'
import { Link } from 'react-router-dom'
function Login() {
  return (
    <div className='w-full lg:h-[88vh] hidden lg:grid grid-cols-2 gap-4 px-8'>
        <div className="bgcolor rounded-2xl w-full h-full flex justify-center items-center p-12">
            <h1 className="text-white text-[3rem] font-semibold ">Start your day <span className='font-thin italic'>automated</span> with <span className=''>Timely</span></h1>
        </div>
        <div className="w-full h-full rounded-2xl flex justify-center items-center ">
            <div className="w-[60%] ">
            <h1 className="text-[2rem] font-semibold text-white">Already A User?<span className='text-[.6rem] font-thin italic'> You need to login</span></h1>
            <form action="get" className="pt-8 text-white">
                <div className="grid mb-10">
                    <label className='text-[1.5rem]'>Username</label>
                    <input type="text" className='custom-input'/>
                </div>
                <div className="grid">
                    <label className='text-[1.5rem]'>Password</label>
                    <input type="password" className='custom-input'/>
                </div>
                <button className='mt-12 rounded-xl p-2 text-center text-[1.2rem] font-semibold text-[#0E0E0E] bg-white w-full'>Login</button>
            </form>
            <p className="text-white mt-4 w-full text-center text-[.8rem] font-thin">New User? <Link className='font-medium'>Register</Link></p>
            </div>
        </div>
    </div>
  )
}

export default Login