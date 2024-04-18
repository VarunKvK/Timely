import React from 'react'
import {Link} from 'react-router-dom'

function navbar() {
  return (
    <div className='h-[2rem] w-full flex justify-between items-center p-8 text-[#FFFF] pt-10'>
      <Link className='font-semibold'>Timely</Link>
      <div className="w-[20%] text-[13px] flex justify-between items-center font-regular">
        <Link className='py-2 px-6 rounded-lg border-[1px] border-[#FFF] cursor-pointer'>template</Link>
        <Link  className='py-2 px-6 rounded-lg bg-[#FFF] text-[#0E0E0E] cursor-pointer'>schedule</Link>
      </div>
    </div>
  )
}

export default navbar