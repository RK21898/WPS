using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Warmtepomp_Simulatie_Prototype
{
    public class Formula
    {
        public decimal COP(decimal powerOutput, decimal addedPower)
        {
            decimal cop;
            return cop = powerOutput / addedPower;
        }

        /// <summary>
        /// Use for both Intake and Output sides in heat pump.
        /// power in Watts
        /// Density in kg/m^3
        /// specific heat in Joule/kg.K
        /// Delta T in Kelvin
        /// </summary>
        /// <param name="power"></param>
        /// <param name="density"></param>
        /// <param name="specific_heat"></param>
        /// <param name="deltaT"></param>
        /// <returns>volume flow rate in m^3/s</returns>
        public decimal WaterFlow(decimal power, decimal density, decimal specific_heat, decimal deltaT)
        {
            decimal qv;
            return qv = power / (density * specific_heat * deltaT);
        }

        /// <summary>
        /// Qw = Warmth delivered to building by heat pump in MWh
        /// Qk = Cold delivered to building by heat pump in MWh
        /// E = Electricity used by the pump system in MWh
        /// G = Electric equivalent of natural gas used by the pump system in MWh 
        /// </summary>
        /// <param name="Qw"></param>
        /// <param name="Qk"></param>
        /// <param name="E"></param>
        /// <param name="G"></param>
        /// <returns>Seasonal Performance Factor</returns>
        public decimal SeasonalPerformanceFactor(decimal Qw, decimal Qk, decimal E, decimal G)
        {
            decimal spf;
            return spf = (Qw + Qk) / (E + G);
        }
    }
}
