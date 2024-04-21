import React from 'react'

function Login() {
  return (
    <div className='w-full lg:h-[88vh] hidden lg:grid grid-cols-2 gap-4'>
        <div className="bgcolor rounded-2xl w-full h-full">
            Hello
        </div>
        <div className="w-full h-full flex justify-center items-center ">
            <div className="w-[60%] ">
            <h1 className="text-[2rem] font-semibold text-white">New User?<span className='text-[.6rem] font-medium'> You need to login</span></h1>
            <form action="" className="pt-8 text-white">
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
            </div>
        </div>
    </div>
  )
}

export default Login