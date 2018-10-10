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
        /// watts per square meter collected by horizontal collector
        /// </summary>
        public Dictionary<string, int> HorizontalCollectorInfo = new Dictionary<string, int>()
        {
            {"Droge zanderige bodem", 50},
            {"Goed", 60},
            {"Normaal", 70},
            {"Slecht", 80}
        };

        /// <summary>
        /// watts per meter collected by vertical collector
        /// </summary>
        public Dictionary<string, int> VerticalCollectorInfo = new Dictionary<string, int>()
        {
            {"Droog sediment", 50},
            {"Goed", 60},
            {"Normaal", 70},
            {"Slecht", 80}
        }; 

        // finish inputting data into these dictionaries
    }
}
