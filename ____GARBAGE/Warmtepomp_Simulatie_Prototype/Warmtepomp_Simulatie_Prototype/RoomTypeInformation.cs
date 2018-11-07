using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Warmtepomp_Simulatie_Prototype
{
    public class RoomTypeInformation
    {
        /// <summary>
        /// watts per square meter used to warm a room of x m^3 at a standard
        /// of 22 degrees prior to corrections
        /// </summary>
        public Dictionary<string, int> RoomTypeInfo = new Dictionary<string, int>()
        {
            {"Excellent", 50},
            {"Goed", 60},
            {"Normaal", 70},
            {"Slecht", 80}
        };
    }
}
