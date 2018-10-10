using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Warmtepomp_Simulatie_Prototype
{
    public class SoilTypeInformation
    {
        /// <summary>
        /// watts per square meter collected by the heat pump
        /// in different soil types
        /// </summary>
        public Dictionary<string, int> HorizontalSoilTypes = new Dictionary<string, int>()
        {
            {"Droge zanderige bodem", 50},
            {"Vochtige zanderige bodem", 60},
            {"Normaal", 70},
            {"Slecht", 80}
        }; //Incomplete, add vertical collector soil types and finish horizontal collector types
    }
}
